from pydantic import BaseModel

class UserCreate(BaseModel):
    correo: str
    contrasenia: str
