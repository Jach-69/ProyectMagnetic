from .. import db

class Bloque(db.Model):
    __tablename__ = 'bloques'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre_bloque = db.Column(db.String(255), nullable=False)
    campus_id = db.Column(db.Integer, db.ForeignKey('campus.id', ondelete='CASCADE'))

    aulas = db.relationship('Aula', backref='bloque', lazy=True)
