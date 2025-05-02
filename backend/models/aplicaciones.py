from sqlalchemy import Column,Column, Date, ForeignKey, Uuid, String
from database import Base  # ← usamos Base
from sqlalchemy.orm import relationship

# para instalar sqlalchemy :          pip install sqlalchemy
# o si de esta manera no funciona: python -m pip install sqlalchemy


class Aplicacion(Base):
    __tablename__ = "aplicaciones"
    __table_args__ = {"schema": "core"}

    id_aplicante = Column(Uuid, ForeignKey("core.aplicantes.id"), primary_key=True)
    id_oferta = Column(Uuid, ForeignKey("core.ofertas.id"), primary_key=True)
    fecha_aplicacion = Column(Date, nullable=False)
    id_estado = Column(Uuid, ForeignKey("core.estados.id"), nullable=False)

    # Relaciones (opcional, si tienes modelos definidos para estas tablas)
    aplicante = relationship("Aplicante")
    oferta = relationship("Oferta")
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
    cv = Column(String(100), nullable=False)

