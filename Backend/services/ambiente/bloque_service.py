from models.ambiente.bloque import Bloque  # Asegúrate de que la importación sea correcta
from models import db

class BloqueService:
    @staticmethod
    def create_bloque(data):
        nuevo_bloque = Bloque(**data)
        db.session.add(nuevo_bloque)
        db.session.commit()
        return nuevo_bloque

    @staticmethod
    def get_bloques():
        return [{'id': b.id, 'nombre_bloque': b.nombre_bloque, 'campus_id': b.campus_id} for b in Bloque.query.all()]

    @staticmethod
    def get_bloque(id):
        bloque = Bloque.query.get(id)
        if bloque:
            return {'id': bloque.id, 'nombre_bloque': bloque.nombre_bloque, 'campus_id': bloque.campus_id}
        return None

    @staticmethod
    def update_bloque(id, data):
        bloque = Bloque.query.get(id)
        if bloque:
            for key, value in data.items():
                setattr(bloque, key, value)
            db.session.commit()
            return bloque
        return None

    @staticmethod
    def delete_bloque(id):
        bloque = Bloque.query.get(id)
        if bloque:
            db.session.delete(bloque)
            db.session.commit()
            return True
        return False
