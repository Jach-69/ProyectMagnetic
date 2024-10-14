# services/ambiente/campus_service.py
from models import db, Campus

def add_campus(data):
    nuevo_campus = Campus(**data)
    db.session.add(nuevo_campus)
    db.session.commit()
    return nuevo_campus

def get_all_campus():
    return Campus.query.all()

def get_campus_by_id(id):
    return Campus.query.get(id)

def update_campus_data(id, data):
    campus = Campus.query.get(id)
    if campus:
        for key, value in data.items():
            setattr(campus, key, value)
        db.session.commit()
        return campus
    return None

def delete_campus_data(id):
    campus = Campus.query.get(id)
    if campus:
        db.session.delete(campus)
        db.session.commit()
        return campus
    return None
