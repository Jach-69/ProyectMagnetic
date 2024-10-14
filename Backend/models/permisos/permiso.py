from .. import db

class PermisoAcceso(db.Model):
    __tablename__ = 'permisos_acceso'
    
    id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('personas.id', ondelete='CASCADE'))
    aula_id = db.Column(db.Integer, db.ForeignKey('aulas.id', ondelete='CASCADE'))
    es_universal = db.Column(db.Boolean, default=False)
