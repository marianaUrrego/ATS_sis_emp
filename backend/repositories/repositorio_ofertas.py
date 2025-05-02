from models.ofertas import Oferta , Departamento
from sqlalchemy import text, Uuid, func
from sqlalchemy.orm import joinedload

class OfertasRepository:
    

    def __init__(self, db_session):
        self.db = db_session

    def get_all_offers(self):
         return self.db.query(Oferta).options(joinedload(Oferta.departamento)).all()

    def get_Oferta_by_id(self, uuid : Uuid):
        return self.db.query(Oferta).filter(Oferta.id == uuid).first()
    
    def get_oferta_by_name(self, nombre: str):
        return self.db.query(Oferta).filter(func.lower(Oferta.nombre) == nombre.lower()).first()

    def insertar_oferta(self, nombre: str, departamento: str, perfil: str):

        query = text("CALL core.p_insertar_oferta(:param_nombre, :param_departamento, :param_perfil)")
        self.db.execute(query, {
            "param_nombre": nombre,
            "param_departamento": departamento,
            "param_perfil": perfil
        })
        self.db.commit()
        return "oferta creada exitosamente"

class DepartamentoRepository:
    def __init__(self, db_session):
        self.db = db_session

    def get_all_departamentos(self):
        return self.db.query(Departamento).all()

    def get_departamento_by_id(self, uuid : Uuid):
        dep = self.db.query(Departamento).filter(Departamento.id == uuid).first()
        return dep.nombre if dep else None
    
    def get_departamento_by_name(self, nombre: str):
        return self.db.query(Departamento).filter(func.lower(Departamento.nombre) == nombre.lower()).first()

    def insertar_Departamento(self, nombre: str):

        query = text("CALL core.p_insertar_departamento(:param_nombre)")
        self.db.execute(query, {
            "param_nombre": nombre,
        })
        self.db.commit()
        return ("departamento creado correctamente")