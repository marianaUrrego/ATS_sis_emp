from fastapi import APIRouter, Depends
from fastapi import HTTPException
from fastapi import  File, UploadFile, Form
from database import SessionLocal
from azure.storage.blob import BlobServiceClient
from sqlalchemy.orm import Session
import shutil
import os
from uuid import UUID 
from repositories.repositorio_aplicante import AplicanteRepository
from models.aplicaciones import Aplicacion, Aplicante
from models.ofertas import Oferta
from schemas.shemas import AplicacionResponse
from typing import List
from dotenv import load_dotenv
from utils.pdf_utils import extraer_texto_pdf
from utils.gemini_handler import coordinar_peticion


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(prefix="/aplicaciones", tags=["Aplicaciones"])

# Tu cadena de conexión
load_dotenv()  # carga desde .env

azure_connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = "hojas-de-vida"

blob_service_client = BlobServiceClient.from_connection_string(azure_connection_string)

# función para guardar el archivo en el blob
def upload_file_to_blob(file_path, blob_name) -> str:
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    print(f"Archivo subido como: {blob_name}")
    blob_url = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{blob_name}"
    return blob_url


# función para insertar una oferta
import os
import shutil
import uuid
from fastapi import HTTPException, File, UploadFile, Depends, Form
from sqlalchemy.orm import Session

@router.post("/")
def insertar_aplicación(
    db: Session = Depends(get_db),
    nombre: str = Form(...),
    correo: str = Form(...),
    id_oferta: str = Form(...),
    file: UploadFile = File(...)
):
    try:
        # Generar un nombre de archivo único
        unique_filename = f"{uuid.uuid4()}_{file.filename}"
        
        # Crear directorio temporal
        os.makedirs("temp", exist_ok=True)
        
        # Ruta completa del archivo
        file_location = os.path.join("temp", unique_filename)
        
        try:
            # Guardar el archivo
            with open(file_location, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            
            # Convertir id_oferta a UUID
            id_oferta_uuid = uuid.UUID(id_oferta)
            
            # Extraer texto del PDF
            texto_cv = extraer_texto_pdf(file_location)
            
            # Obtener oferta de la base de datos
            oferta = db.query(Oferta).filter(Oferta.id == id_oferta_uuid).first()
            if not oferta:
                raise HTTPException(status_code=404, detail="Oferta no encontrada")
            
            # Obtener texto de la oferta
            texto_oferta = oferta.perfil
            
            # Subir archivo a blob storage
            cv_url = upload_file_to_blob(file_location, unique_filename)
            
            # Preparar repositorio
            aplicacion_repo = AplicanteRepository(db)
            
            # Crear aplicación con el estado determinado
            aplicacion = Aplicacion()
            aplicacion.id_oferta = id_oferta_uuid
            aplicacion.id_estado = coordinar_peticion(texto_cv, texto_oferta)
            
            # Crear aplicante
            aplicante = Aplicante()
            aplicante.nombre = nombre
            aplicante.correo = correo
            aplicante.cv = cv_url
            
            # Insertar aplicación
            msg = aplicacion_repo.Insertar_aplicación(aplicante, aplicacion)
            
            return msg
        
        except Exception as e:
            # Manejar errores de procesamiento
            raise HTTPException(status_code=500, detail=f"Error processing application: {str(e)}")
        
        finally:
            # Limpiar archivo temporal
            try:
                os.remove(file_location)
            except Exception as remove_error:
                print(f"Could not remove temporary file: {remove_error}")
    
    except Exception as e:
        # Manejar errores de carga de archivo
        raise HTTPException(status_code=400, detail=f"File upload error: {str(e)}")

@router.get("/", response_model=List[AplicacionResponse])
def get_all_ofertas(db=Depends(get_db)):
    
    aplicacion_repo = AplicanteRepository(db)
    aplicaciones= aplicacion_repo.get_all_aplicants()
    return [
        AplicacionResponse(
            nombre_aplicante= aplicacion.aplicante.nombre,
            correo= aplicacion.aplicante.correo,
            id_oferta= aplicacion.id_oferta,
            oferta = aplicacion.oferta.nombre,
            id_estado=aplicacion.id_estado,
            estado = aplicacion.estado.nombre
        )
        for aplicacion in aplicaciones
    ]
    
from fastapi import Query

@router.get("/cv", summary="Obtener URLs de CVs por correo", response_model=List[str])
def obtener_cvs_por_correo(correo: str = Query(...), db: Session = Depends(get_db)):
    aplicacion_repo = AplicanteRepository(db)
    aplicaciones = aplicacion_repo.get_all_aplicants()

    cvs = [
        aplicacion.aplicante.cv
        for aplicacion in aplicaciones
        if aplicacion.aplicante.correo == correo
    ]

    if not cvs:
        raise HTTPException(status_code=404, detail="No se encontraron CVs para este correo")

    return cvs