from sqlalchemy import Column, String, Uuid, ForeignKey, Date
from database import Base
from sqlalchemy.orm import relationship

class Oferta(Base):
    __tablename__ = "ofertas"
    __table_args__ = {"schema": "core"}

    id = Column(Uuid, primary_key=True)
    nombre = Column(Uuid, unique=True)
    id_departamento = Column(Uuid, ForeignKey('core.departamentos.id'))
    perfil = Column(String)
    fecha_creacion = Column(Date, nullable=False)
   
    departamento = relationship("Departamento")
    aplicaciones = relationship("Aplicacion", back_populates="oferta")

class Departamento(Base):
    __tablename__ = "departamentos"
    __table_args__ = {"schema": "core"}

    id = Column(Uuid, primary_key=True)
    nombre = Column(Uuid, unique=True)