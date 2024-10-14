from .. import db

class Campus(db.Model):
    __tablename__ = 'campus'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre_campus = db.Column(db.String(255), nullable=False)

    bloques = db.relationship('Bloque', backref='campus', lazy=True)
