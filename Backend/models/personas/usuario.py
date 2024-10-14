from .. import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('personas.id', ondelete='CASCADE'))
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
