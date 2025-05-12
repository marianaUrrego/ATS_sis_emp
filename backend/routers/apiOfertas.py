from fastapi import APIRouter, Depends
from fastapi import HTTPException
from database import SessionLocal
from repositories.repositorio_ofertas import DepartamentoRepository, OfertasRepository
from schemas.shemas import OfertaCreate, Departamentos, OfertaMostrar
from typing import List
from sqlalchemy.orm import Session

router = APIRouter(prefix="/ofertas", tags=["Ofertas"])

# Dependencia para la sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/departamento/{nombre}")
def create_departamento(nombre, db=Depends(get_db)):
    departamento_repo = DepartamentoRepository(db)
    msg = departamento_repo.insertar_Departamento(nombre)
    return msg

@router.get("/departamentos/",  response_model=List[Departamentos])
def get_all_departamentos(db = Depends(get_db)):
    dep_repo = DepartamentoRepository(db)
    departamentos= dep_repo.get_all_departamentos()
    return departamentos

@router.post("/")
def create_oferta(oferta : OfertaCreate, db=Depends(get_db)):
    oferta_repo = OfertasRepository(db)
    dep_repo = DepartamentoRepository(db)
    departamento = dep_repo.get_departamento_by_name(oferta.departamento)
    if not departamento:
        raise HTTPException(status_code=404, detail="El departamento no existe")

    msg=  oferta_repo.insertar_oferta(oferta.nombre, oferta.departamento, oferta.perfil)
    if(msg):
        id_oferta = oferta_repo.get_oferta_by_name(oferta.nombre)
        oferta_repo.insertar_requisitos_oferta(
            id_oferta.id,
            oferta.habilidades_blandas,
            oferta.habilidades_tecnicas,
            oferta.titulos,
            oferta.experiencia)
    return{
        "oferta creada exitosamente"
    }

@router.get("/", response_model=List[OfertaMostrar])
def get_all_ofertas(db=Depends(get_db)):
    oferta_repo = OfertasRepository(db)
    ofertas = oferta_repo.get_all_offers()

    return [
        OfertaMostrar(
            id= oferta.id,
            nombre=oferta.nombre,
            departamento=oferta.departamento.nombre,
            perfil=oferta.perfil,
            fecha_creacion= oferta.fecha_creacion
        )
        for oferta in ofertas
    ]

@router.get("/{idOferta}", response_model=OfertaCreate)
def get_offer_by_id(idOferta, db= Depends(get_db)):
    oferta_repo = OfertasRepository(db)
    oferta = oferta_repo.get_oferta_completa(idOferta)
    return oferta

@router.get("/id/{id_oferta}/aplicantes")
def obtener_aplicantes_por_id_oferta(id_oferta: str, db: Session = Depends(get_db)):
    """
    Endpoint para obtener aplicantes por ID de oferta.
    
    Args:
        id_oferta: El ID de la oferta (UUID en formato string)
        db: Sesión de base de datos
    
    Returns:
        Lista de aplicantes para la oferta especificada
    """
    repo = OfertasRepository(db)
    aplicaciones = repo.get_aplicaciones_por_id_oferta(id_oferta)
    
    return [
        {
            "nombre_aplicante": aplicacion.aplicante.nombre,
            "correo": aplicacion.aplicante.correo,
            "id_oferta": aplicacion.id_oferta,
            "oferta": aplicacion.oferta.nombre,
            "id_estado": aplicacion.id_estado,
            "estado": aplicacion.estado.nombre
        }
        for aplicacion in aplicaciones
    ]


