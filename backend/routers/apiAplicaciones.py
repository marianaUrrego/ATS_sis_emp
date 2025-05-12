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
@router.post("/")
def insertar_aplicación(db=Depends(get_db),
    nombre: str = Form(...),
    correo: str = Form(...),
    id_oferta: str = Form(...),
    file: UploadFile = File(...)):

    id_oferta_uuid = UUID(id_oferta)

    file_location = f"temp/{file.filename}"  # se guarda en una carpeta temporal
    
    aplicacion_repo = AplicanteRepository(db)
    aplicante = Aplicante()
    aplicante.nombre = nombre
    aplicante.correo = correo
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    # Extraer texto de la aplicación del PDF
    texto_cv = extraer_texto_pdf(file_location)
    
    # Obtener texto de la oferta desde la base de datos
    oferta = db.query(Oferta).filter(Oferta.id == id_oferta_uuid).first()
    if not oferta:
        raise HTTPException(status_code=404, detail="Oferta no encontrada")
    
    # Obtener texto de la oferta
    texto_oferta = oferta.perfil

    aplicante.cv = upload_file_to_blob(file_location,file.filename)
    aplication = Aplicacion()
    aplication.id_estado = coordinar_peticion(texto_cv, texto_oferta)
    aplication.id_oferta = id_oferta_uuid

    os.remove(file_location)  # se elimina del almacenamiento local
    msg = aplicacion_repo.Insertar_aplicación(aplicante, aplication)
    return msg


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