from sqlalchemy import Column, String, Uuid, ForeignKey, Date
from database import Base  # ← usamos Base
from sqlalchemy.orm import relationship

# para instalar sqlalchemy :          pip install sqlalchemy
# o si de esta manera no funciona: python -m pip install sqlalchemy


class Oferta(Base):

    __tablename__ = "ofertas"

    id= Column(Uuid,primary_key=True)
    nombre = Column(Uuid, unique=True)
    id_departamento= Column(Uuid, ForeignKey('core.departamentos.id'))
    perfil = Column(String)
    fecha_creacion = Column(Date, nullable=False)
   
    departamento = relationship("Departamento")
    aplicaciones = relationship("Aplicacion")

class Departamento(Base):

    __tablename__ = "departamentos"

    id= Column(Uuid,primary_key=True)
    nombre = Column(Uuid, unique=True)
