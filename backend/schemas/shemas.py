from pydantic import BaseModel
from uuid import UUID 
from typing import List
# python -m pip install uuid

class UserCreate(BaseModel):
    correo: str
    contrasenia: str

class Departamentos(BaseModel):
    id: UUID
    nombre: str

class OfertaCreate(BaseModel):
    nombre: str
    departamento: str
    perfil: str
    habilidades_blandas: List[str]
    habilidades_tecnicas: List[str]
    titulos: List[str]
    experiencia: List[str]

class AplicacionResponse(BaseModel):
    nombre_aplicante: str
    correo: str
    id_oferta: UUID
    oferta: str
    id_estado: UUID
    estado: str
    