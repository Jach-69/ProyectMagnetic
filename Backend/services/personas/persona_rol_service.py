from models import db, PersonaRol

class PersonaRolService:
    @staticmethod
    def create_persona_rol(data):
        nueva_relacion = PersonaRol(**data)
        db.session.add(nueva_relacion)
        db.session.commit()
        return nueva_relacion

    @staticmethod
    def get_persona_roles():
        return PersonaRol.query.all()

    @staticmethod
    def get_persona_rol(id):
        return PersonaRol.query.get(id)

    @staticmethod
    def update_persona_rol(id, data):
        relacion = PersonaRol.query.get(id)
        if relacion:
            for key, value in data.items():
                setattr(relacion, key, value)
            db.session.commit()
            return relacion
        return None

    @staticmethod
    def delete_persona_rol(id):
        relacion = PersonaRol.query.get(id)
        if relacion:
            db.session.delete(relacion)
            db.session.commit()
            return relacion
        return None
