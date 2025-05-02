from models.aplicaciones import Aplicacion, Aplicante
from sqlalchemy import text
from sqlalchemy.orm import joinedload

class AplicanteRepository:
    def __init__(self, db_session):
        self.db = db_session

    def get_all_aplicants(self):
        return self.db.query(Aplicacion).options(joinedload(Aplicacion.oferta), joinedload(Aplicacion.estado),joinedload(Aplicacion.aplicante)).all()


    def Insertar_aplicación(self, aplicante: Aplicante, aplicacion: Aplicacion):
        query = text("CALL core.p_insertar_aplicacion(:param_nombre, :param_correo, :param_cv, :param_id_oferta, :param_id_estado)")
        self.db.execute(query, {
            "param_nombre": aplicante.nombre,
            "param_correo": aplicante.correo,
            "param_cv": aplicante.cv,
            "param_id_oferta": aplicacion.id_oferta,
            "param_id_estado":aplicacion.id_estado

        })
        self.db.commit()
        return "aplicación guardada exitosamente"