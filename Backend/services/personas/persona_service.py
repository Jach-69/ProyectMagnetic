from models import db, Persona
from sqlalchemy.exc import IntegrityError

class PersonaService:
    @staticmethod
    def create_persona(data):
        # Verificar si la clave ya existe
        if Persona.query.filter_by(clave=data['clave']).first():
            raise ValueError("La clave ya está en uso")

        nueva_persona = Persona(**data)
        db.session.add(nueva_persona)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Error al guardar la persona en la base de datos")
        
        return nueva_persona

    @staticmethod
    def get_personas():
        return Persona.query.all()

    @staticmethod
    def get_persona(id):
        return Persona.query.get(id)

    @staticmethod
    def update_persona(id, data):
        persona = Persona.query.get(id)
        if persona:
            for key, value in data.items():
                setattr(persona, key, value)
            db.session.commit()
            return persona
        return None

    @staticmethod
    def delete_persona(id):
        persona = Persona.query.get(id)
        if persona:
            db.session.delete(persona)
            db.session.commit()
            return persona
        return None
