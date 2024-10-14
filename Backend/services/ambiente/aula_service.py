from models import db
from models.ambiente.aula import Aula  # Asegúrate de que esta línea sea correcta

class AulaService:
    @staticmethod
    def create_aula(data):
        nueva_aula = Aula(**data)
        db.session.add(nueva_aula)
        db.session.commit()
        return nueva_aula

    @staticmethod
    def get_aulas():
        return Aula.query.all()  # Esta línea debería funcionar si Aula está correctamente importado

    @staticmethod
    def get_aula(id):
        return Aula.query.get(id)

    @staticmethod
    def update_aula(id, data):
        aula = Aula.query.get(id)
        if aula:
            for key, value in data.items():
                setattr(aula, key, value)
            db.session.commit()
            return aula
        return None

    @staticmethod
    def delete_aula(id):
        aula = Aula.query.get(id)
        if aula:
            db.session.delete(aula)
            db.session.commit()
            return aula
        return None
