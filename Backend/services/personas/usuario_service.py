from models import db, Usuario

class UsuarioService:
    @staticmethod
    def create_usuario(data):
        nuevo_usuario = Usuario(**data)  # Asegúrate de que `data` tenga los campos correctos
        db.session.add(nuevo_usuario)
        db.session.commit()
        return nuevo_usuario

    @staticmethod
    def get_usuarios():
        return Usuario.query.all()

    @staticmethod
    def get_usuario(id):
        return Usuario.query.get(id)

    @staticmethod
    def update_usuario(id, data):
        usuario = Usuario.query.get(id)
        if usuario:
            for key, value in data.items():
                setattr(usuario, key, value)
            db.session.commit()
            return usuario
        return None

    @staticmethod
    def delete_usuario(id):
        usuario = Usuario.query.get(id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return usuario
        return None
