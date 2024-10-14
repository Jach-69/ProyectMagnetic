from models import db, Acceso

class AccesosService:
    @staticmethod
    def get_all_accesos():
        return [{'id': a.id, 'fecha_hora': a.fecha_hora, 'es_valido': a.es_valido, 'usuario_id': a.usuario_id, 'aula_id': a.aula_id} for a in Acceso.query.all()]

    @staticmethod
    def get_acceso_by_id(id):
        acceso = Acceso.query.get(id)
        if acceso:
            return {'id': acceso.id, 'fecha_hora': acceso.fecha_hora, 'es_valido': acceso.es_valido, 'usuario_id': acceso.usuario_id, 'aula_id': acceso.aula_id}
        return None

    @staticmethod
    def create_acceso(data):
        nuevo_acceso = Acceso(**data)
        db.session.add(nuevo_acceso)
        db.session.commit()
        return nuevo_acceso

    @staticmethod
    def delete_acceso(id):
        acceso = Acceso.query.get(id)
        if acceso:
            db.session.delete(acceso)
            db.session.commit()
            return True
        return False
