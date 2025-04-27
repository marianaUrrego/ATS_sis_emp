from fastapi import FastAPI, Depends
from database import SessionLocal
from repositories.repositorio_usuario import UserRepository
from repositories.repositorio_ofertas import DepartamentoRepository, OfertasRepository
from schemas.shemas import UserCreate
from models.usuarios import Usuarios
from typing import List

# para instalar fastapi :          pip install fastapi 
# o si de esta manera no funciona: python -m pip install fastapi

# para instalar uvicorn : python -m pip install uvicorn    
# python -m pip install psycopg2 : esto también se necesita, aunque no se muy bien paque



app = FastAPI()

# Dependencia para la sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return "esta es la API"


@app.post("/Usuarios/")
def create_product(usuario: UserCreate, db=Depends(get_db)):
    user_repo = UserRepository(db)
    new_User = Usuarios(correo = usuario.correo, contrasenia = usuario.contrasenia)
    new_User = user_repo.create_users(new_User)
    return {
        "correo": new_User.correo,
        "contraseña": new_User.contrasenia
    }

@app.get("/Usuarios/", response_model=List[UserCreate])
def get_all_users(db=Depends(get_db)):
    user_repo = UserRepository(db)
    usuarios = user_repo.get_all_users()
    return usuarios

@app.get("/Usuarios/{email}", response_model=UserCreate)
def get_user_by_email (email, db=Depends(get_db)):
    user_repo = UserRepository(db)
    usuario = user_repo.get_user_by_email(email)
    return usuario

@app.post("/Departamentos/{nombre}")
def create_departamento(nombre, db=Depends(get_db)):
    departamento_repo = DepartamentoRepository(db)
    nuevo_dep = departamento_repo.insertar_Departamento(nombre)
    return nuevo_dep

#para iniciar el servidor se usa python -m uvicorn api:app --reload     