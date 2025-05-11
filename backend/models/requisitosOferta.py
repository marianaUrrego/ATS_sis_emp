from sqlalchemy import Column, String, ForeignKey, Table, Date, Uuid, Integer, Text
from sqlalchemy.orm import relationship
from database import Base

class HabilidadTecnica(Base):
    __tablename__ = "habilidades_tecnicas"

    id = Column(Uuid, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)


class HabilidadTecnicaXOferta(Base):
    __tablename__ = "habilidades_tecnicasxoferta"

    id_oferta = Column(Uuid, ForeignKey("core.ofertas.id"), primary_key=True)
    id_hab_tecnica = Column(Uuid, ForeignKey("core.habilidades_tecnicas.id"), primary_key=True)


class HabilidadBlanda(Base):
    __tablename__ = "habilidades_blandas"

    id = Column(Uuid, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)


class HabilidadBlandaXOferta(Base):
    __tablename__ = "habilidades_blandasxoferta"

    id_oferta = Column(Uuid, ForeignKey("core.ofertas.id"), primary_key=True)
    id_hab_blanda = Column(Uuid, ForeignKey("core.habilidades_blandas.id"), primary_key=True)

class Titulo(Base):
    __tablename__ = "titulos"

    id = Column(Uuid, primary_key=True)
    nombre = Column(String(50), unique=True, nullable=False)


class TituloXOferta(Base):
    __tablename__ = "titulosxoferta"

    id_oferta = Column(Uuid, ForeignKey("core.ofertas.id"), primary_key=True)
    id_titulo = Column(Uuid, ForeignKey("core.titulos.id"), primary_key=True)

class Experiencia(Base):
    __tablename__ = "experiencia"

    id_oferta = Column(Uuid, ForeignKey("core.ofertas.id"), primary_key=True)
    descripcion = Column(Text, primary_key=True)