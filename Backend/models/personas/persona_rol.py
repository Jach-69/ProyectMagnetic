from .. import db

class PersonaRol(db.Model):
    __tablename__ = 'persona_rol'
    
    id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('personas.id', ondelete='CASCADE'))
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id', ondelete='CASCADE'))
