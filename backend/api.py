from fastapi import FastAPI, Depends
from database import SessionLocal
from repositories.repositorio_usuario import UserRepository
from schemas.shemas import UserCreate
from models.usuarios import Usuarios

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


@app.post("/products/")
def create_product(product: UserCreate, db=Depends(get_db)):
    user_repo = UserRepository(db)
    new_User = Usuarios(correo = product.correo, contrasenia = product.contraseña)
    new_User = user_repo.create_users(new_User)
    return {
        "correo": new_User.correo,
        "contraseña": new_User.contrasenia
    }

#para iniciar el servidor se usa python -m uvicorn api:app --reload     