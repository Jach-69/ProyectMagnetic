from mainApp import app
from models import db

# Función para crear la base de datos
def create_database():
    with app.app_context():
        db.create_all()
        print("Base de datos creada.")

# No es necesario tener un bloque `if __name__ == "__main__":` aquí
