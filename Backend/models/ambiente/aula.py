from .. import db

class Aula(db.Model):
    __tablename__ = 'aulas'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre_aula = db.Column(db.String(255), nullable=False)
    bloque_id = db.Column(db.Integer, db.ForeignKey('bloques.id', ondelete='CASCADE'))

    permisos_acceso = db.relationship('PermisoAcceso', backref='aula', lazy=True)
