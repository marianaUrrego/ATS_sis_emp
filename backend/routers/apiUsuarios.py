from fastapi import APIRouter, Depends
from database import SessionLocal
from repositories.repositorio_usuario import UserRepository
from repositories.repositorio_ofertas import DepartamentoRepository, OfertasRepository
from schemas.shemas import UserCreate
from models.usuarios import Usuarios
from typing import List
import bcrypt

# para instalar fastapi :          pip install fastapi 
# o si de esta manera no funciona: python -m pip install fastapi

# para instalar uvicorn : python -m pip install uvicorn    
# python -m pip install psycopg2 : esto también se necesita, aunque no se muy bien paque

def hash_password(plain_password: str) -> str:
    return bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# Dependencia para la sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_user(usuario: UserCreate, db=Depends(get_db)):
    user_repo = UserRepository(db)
    hashed_password = hash_password(usuario.contrasenia)
    new_User = Usuarios(correo = usuario.correo, contrasenia = hashed_password)
    new_User = user_repo.create_users(new_User)
    return {
        "correo": new_User.correo,
        "contraseña": new_User.contrasenia
    }

@router.get("/", response_model=List[UserCreate])
def get_all_users(db=Depends(get_db)):
    user_repo = UserRepository(db)
    usuarios = user_repo.get_all_users()
    return usuarios

@router.get("/{email}", response_model=UserCreate)
def get_user_by_email (email, db=Depends(get_db)):
    user_repo = UserRepository(db)
    usuario = user_repo.get_user_by_email(email)
    return usuario

#para iniciar el servidor se usa python -m uvicorn api:app --reload     