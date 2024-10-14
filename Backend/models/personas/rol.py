from .. import db

class Rol(db.Model):
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre_rol = db.Column(db.String(255), unique=True, nullable=False)

    personas = db.relationship('PersonaRol', backref='rol', lazy=True)
