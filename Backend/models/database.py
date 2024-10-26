from .db import db

def create_database():
    db.create_all()  # Crea todas las tablas definidas
    print("Base de datos creada con éxito.")  # Mensaje de confirmación
