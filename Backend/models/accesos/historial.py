from .. import db

class HistorialAcceso(db.Model):
    __tablename__ = 'historial_accesos'
    
    id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('personas.id'), nullable=False)
    aula_id = db.Column(db.Integer, db.ForeignKey('aulas.id'), nullable=False)
    fecha_hora = db.Column(db.DateTime, default=db.func.current_timestamp())
    es_valido = db.Column(db.Boolean, nullable=False)
