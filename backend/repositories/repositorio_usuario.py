from models.usuarios import Usuarios

class UserRepository:
    def __init__(self, db_session):
        self.db = db_session

    def get_all_users(self):
        return self.db.query(Usuarios).all()

    def get_user_by_email(self, email):
        return self.db.query(Usuarios).filter(Usuarios.correo ==email).first()

    def create_users(self, usuario):
        new_user = usuario
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
