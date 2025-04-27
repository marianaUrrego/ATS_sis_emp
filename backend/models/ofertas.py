from sqlalchemy import Column, String, Uuid
from database import Base  # ← usamos Base

# para instalar sqlalchemy :          pip install sqlalchemy
# o si de esta manera no funciona: python -m pip install sqlalchemy


class Oferta(Base):

    __tablename__ = "ofertas"

    id= Column(Uuid,primary_key=True)
    nombre = Column(Uuid, unique_key=True)
    id_departamento= Column(Uuid)
    perfil = Column(String)

class Departamento(Base):

    __tablename__ = "departamentos"

    id= Column(Uuid,primary_key=True)
    nombre = Column(Uuid, unique_key=True)