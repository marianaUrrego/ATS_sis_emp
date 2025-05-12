from sqlalchemy import Column, Date, ForeignKey, Uuid, String, Integer
from database import Base
from sqlalchemy.orm import relationship

class Aplicacion(Base):
    __tablename__ = "aplicaciones"
    __table_args__ = {"schema": "core"}

    id_aplicante = Column(Uuid, ForeignKey("core.aplicantes.id"), primary_key=True)
    id_oferta = Column(Uuid, ForeignKey("core.ofertas.id"), primary_key=True)
    fecha_aplicacion = Column(Date, nullable=False)
    id_estado = Column(Integer, ForeignKey("core.estados.id"), nullable=False)

    # Relaciones con back_populates
    aplicante = relationship("Aplicante")
    oferta = relationship("Oferta", back_populates="aplicaciones")
    estado = relationship("Estado")

class Estado(Base):
    __tablename__ = "estados"
    __table_args__ = {"schema": "core"}

    id = Column(Uuid, primary_key=True)
    nombre = Column(String(30), nullable=False, unique=True)

class Aplicante(Base):
    __tablename__ = "aplicantes"
    __table_args__ = {"schema": "core"}

    id = Column(Uuid, primary_key=True)
    nombre = Column(String(30), nullable=False)
    correo = Column(String(100), nullable=False, unique=True)
    cv = Column(String(500), nullable=False)