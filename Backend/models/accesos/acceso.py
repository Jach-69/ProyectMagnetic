from .. import db

class Acceso(db.Model):
    __tablename__ = 'accesos'
    
    id = db.Column(db.Integer, primary_key=True)
    fecha_hora = db.Column(db.DateTime, default=db.func.current_timestamp())
    es_valido = db.Column(db.Boolean, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    aula_id = db.Column(db.Integer, db.ForeignKey('aulas.id'))
