from backend.models.aplicantes import Aplicantes

class ProductRepository:
    def __init__(self, db_session):
        self.db = db_session

    def get_all_aplicants(self):
        return self.db.query(Aplicantes).all()



    def create_product(self, aplicante : Aplicantes):
        new_aplicante = aplicante
        self.db.add(new_aplicante)
        self.db.commit()
        self.db.refresh(new_aplicante)
        return new_aplicante
