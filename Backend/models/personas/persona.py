from .. import db

class Persona(db.Model):
    __tablename__ = 'personas'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    tarjeta_rfid = db.Column(db.String(255), unique=True, nullable=False)
    clave = db.Column(db.String(255), nullable=False)
    nombre_usuario = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    usuarios = db.relationship('Usuario', backref='persona', lazy=True)
    permisos_acceso = db.relationship('PermisoAcceso', backref='persona', lazy=True)
    roles = db.relationship('PersonaRol', backref='persona', lazy=True)
