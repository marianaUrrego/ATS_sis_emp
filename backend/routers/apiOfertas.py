from fastapi import APIRouter, Depends
from fastapi import HTTPException
from database import SessionLocal
from repositories.repositorio_ofertas import DepartamentoRepository, OfertasRepository
from schemas.shemas import OfertaCreate, Departamentos
from typing import List

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
            id_oferta,
            oferta.habilidades_blandas,
            oferta.habilidades_tecnicas,
            oferta.titulos,
            oferta.experiencia)
    return{
        "oferta creada exitosamente"
    }

@router.get("/", response_model=List[OfertaCreate])
def get_all_ofertas(db=Depends(get_db)):
    oferta_repo = OfertasRepository(db)
    ofertas = oferta_repo.get_all_offers()

    return [
        OfertaCreate(
            nombre=oferta.nombre,
            departamento=oferta.departamento.nombre,
            perfil=oferta.perfil
        )
        for oferta in ofertas
    ]

