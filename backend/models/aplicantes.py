from sqlalchemy import Column, Integer, String, Uuid
from backend.database import Base  # ← usamos Base

# para instalar sqlalchemy :          pip install sqlalchemy
# o si de esta manera no funciona: python -m pip install sqlalchemy


class Aplicantes(Base):

    __tablename__ = "aplicantes"

    id = Column(Uuid, primary_key=True)
    nombre = Column(String, unique=True)
    correo = Column(String, unique=True, index=True)
    cv = Column(String)