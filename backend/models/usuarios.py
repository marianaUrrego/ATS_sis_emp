from sqlalchemy import Column, Integer, String, Uuid
from database import Base  # ← usamos Base

# para instalar sqlalchemy :          pip install sqlalchemy
# o si de esta manera no funciona: python -m pip install sqlalchemy


class Usuarios(Base):

    __tablename__ = "usuarios"

    correo = Column(String, unique=True, primary_key=True)
    contrasenia = Column(String)