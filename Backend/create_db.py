from mainApp import app  # Asegúrate de importar tu aplicación
from models import create_database

if __name__ == "__main__":
    with app.app_context():  # Crea el contexto de la aplicación
        create_database()
