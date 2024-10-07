from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Persona(db.Model):
    __tablename__ = 'personas'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    tarjeta_rfid = db.Column(db.String(255), unique=True, nullable=False)
    clave = db.Column(db.String(255), nullable=False)
    nombre_usuario = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Rol(db.Model):
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre_rol = db.Column(db.String(255), unique=True, nullable=False)

class Campus(db.Model):
    __tablename__ = 'campus'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre_campus = db.Column(db.String(255), nullable=False)

class Bloque(db.Model):
    __tablename__ = 'bloques'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre_bloque = db.Column(db.String(255), nullable=False)
    campus_id = db.Column(db.Integer, db.ForeignKey('campus.id', ondelete='CASCADE'))
    campus = db.relationship('Campus', backref='bloques')

class Aula(db.Model):
    __tablename__ = 'aulas'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre_aula = db.Column(db.String(255), nullable=False)
    bloque_id = db.Column(db.Integer, db.ForeignKey('bloques.id', ondelete='CASCADE'))
    bloque = db.relationship('Bloque', backref='aulas')
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('personas.id', ondelete='CASCADE'))
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

class Acceso(db.Model):
    __tablename__ = 'accesos'
    
    id = db.Column(db.Integer, primary_key=True)
    fecha_hora = db.Column(db.DateTime, default=db.func.current_timestamp())
    es_valido = db.Column(db.Boolean, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    aula_id = db.Column(db.Integer, db.ForeignKey('aulas.id'))

class HistorialAcceso(db.Model):
    __tablename__ = 'historial_accesos'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    aula_id = db.Column(db.Integer, db.ForeignKey('aulas.id'), nullable=False)
    fecha_hora = db.Column(db.DateTime, default=db.func.current_timestamp())
    es_valido = db.Column(db.Boolean, nullable=False)

class PermisoAcceso(db.Model):
    __tablename__ = 'permisos_acceso'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id', ondelete='CASCADE'))
    aula_id = db.Column(db.Integer, db.ForeignKey('aulas.id', ondelete='CASCADE'))
