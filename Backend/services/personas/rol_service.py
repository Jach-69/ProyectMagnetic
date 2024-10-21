from models.personas.rol import Rol
from models import db, Rol

class RolService:
    @staticmethod
    def create_rol(data):
        nuevo_rol = Rol(**data)
        db.session.add(nuevo_rol)
        db.session.commit()
        return nuevo_rol

    @staticmethod
    def get_roles():
        return Rol.query.all()

    @staticmethod
    def get_rol(id):
        return Rol.query.get(id)

    @staticmethod
    def update_rol(id, data):
        rol = Rol.query.get(id)
        if rol:
            for key, value in data.items():
                setattr(rol, key, value)
            db.session.commit()
            return rol
        return None

    @staticmethod
    def delete_rol(id):
        rol = Rol.query.get(id)
        if rol:
            db.session.delete(rol)
            db.session.commit()
            return rol
        return None
