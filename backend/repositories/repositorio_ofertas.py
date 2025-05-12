from models.ofertas import Oferta , Departamento
from models.aplicaciones import Aplicacion
from sqlalchemy import text, Uuid, func
from sqlalchemy.orm import joinedload
from models.requisitosOferta import HabilidadTecnica, HabilidadBlanda, Titulo, Experiencia
from models.requisitosOferta import HabilidadTecnicaXOferta, HabilidadBlandaXOferta, TituloXOferta


class OfertasRepository:

    def __init__(self, db_session):
        self.db = db_session

    def get_all_offers(self):
         return self.db.query(Oferta).options(joinedload(Oferta.departamento)).all()

    def get_Oferta_by_id(self, uuid : Uuid):
        return self.db.query(Oferta).filter(Oferta.id == uuid).first()
    
    def get_oferta_by_name(self, nombre: str):
        return self.db.query(Oferta).filter(func.lower(Oferta.nombre) == nombre.lower()).first()
    
    def get_oferta_completa(self, id_oferta: str):
        # 1. Obtener la oferta principal
        oferta = self.db.query(Oferta).options(joinedload(Oferta.departamento)).filter(Oferta.id == id_oferta).first()
        if not oferta:
            return None

        # 2. Obtener habilidades técnicas
        habilidades_tecnicas = (
            self.db.query(HabilidadTecnica)
            .join(HabilidadTecnicaXOferta, HabilidadTecnica.id == HabilidadTecnicaXOferta.id_hab_tecnica)
            .filter(HabilidadTecnicaXOferta.id_oferta == id_oferta)
            .all()
        )

        # 3. Obtener habilidades blandas
        habilidades_blandas = (
            self.db.query(HabilidadBlanda)
            .join(HabilidadBlandaXOferta, HabilidadBlanda.id == HabilidadBlandaXOferta.id_hab_blanda)
            .filter(HabilidadBlandaXOferta.id_oferta == id_oferta)
            .all()
        )

        # 4. Obtener títulos
        titulos = (
            self.db.query(Titulo)
            .join(TituloXOferta, Titulo.id == TituloXOferta.id_titulo)
            .filter(TituloXOferta.id_oferta == id_oferta)
            .all()
        )

        # 5. Obtener experiencia
        experiencia = (
            self.db.query(Experiencia)
            .filter(Experiencia.id_oferta == id_oferta)
            .all()
        )

        return {
            "nombre": oferta.nombre,
            "departamento": oferta.departamento.nombre,
            "perfil": oferta.perfil,
            "habilidades_tecnicas": [h.nombre for h in habilidades_tecnicas],
            "habilidades_blandas": [h.nombre for h in habilidades_blandas],
            "titulos": [t.nombre for t in titulos],
            "experiencia": [e.descripcion for e in experiencia],
        }

    def insertar_oferta(self, nombre: str, departamento: str, perfil: str):

        query = text("CALL core.p_insertar_oferta(:param_nombre, :param_departamento, :param_perfil)")
        self.db.execute(query, {
            "param_nombre": nombre,
            "param_departamento": departamento,
            "param_perfil": perfil
        })
        self.db.commit()
        return True
    
    def insertar_requisitos_oferta(self,id_oferta, habilidades_blandas, habilidades_tecnicas,titulos, experiencia):

        query = text("CALL core.insertar_requisitos_oferta(:param_id_oferta, :param_habilidades_blandas ,:param_habilidades_tecnicas, :param_titulos, :param_experiencia)")
        self.db.execute(query, {
            "param_id_oferta": id_oferta,
            "param_habilidades_blandas": habilidades_blandas,
            "param_habilidades_tecnicas": habilidades_tecnicas,
            "param_titulos": titulos,
            "param_experiencia": experiencia
        })
        self.db.commit()
        return True
    
    def get_aplicaciones_por_id_oferta(self, id_oferta: str):
        """
        Obtiene todas las aplicaciones para una oferta específica usando el ID.
        
        Args:
            id_oferta: El ID de la oferta en formato string (se convertirá a UUID)
        
        Returns:
            Lista de aplicaciones para la oferta especificada
        """
        import uuid
        
        try:
            # Convertir el string a UUID
            oferta_uuid = uuid.UUID(id_oferta)
        except ValueError:
            # Retornar lista vacía si el ID no es un UUID válido
            return []
            
        return (
            self.db.query(Aplicacion)
            .join(Oferta, Aplicacion.id_oferta == Oferta.id)
            .filter(Oferta.id == oferta_uuid)  # Filtrar por ID en lugar de nombre
            .options(
                joinedload(Aplicacion.aplicante),
                joinedload(Aplicacion.estado),
                joinedload(Aplicacion.oferta)
            )
            .all()
        )

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