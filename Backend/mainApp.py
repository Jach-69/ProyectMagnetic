import logging  # Agrega esta línea al principio
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from config import Config
from models.db import db

# Importar blueprints
from routes.auth import auth_bp
from routes.validate import validate_bp
from routes.personas.personas import personas_bp
from routes.accesos.acceso import accesos_bp
from routes.personas.roles import roles_bp
from routes.ambiente.aulas import aulas_bp
from routes.ambiente.campus import campus_bp
from routes.ambiente.bloques import bloques_bp 
from routes.personas.usuarios import usuarios_bp
from routes.accesos.historial import historial_bp
from routes.permisos.permisos import permisos_bp
from routes.personas.persona_rol import persona_rol_bp

app = Flask(__name__)
app.config.from_object(Config)

# Configuración de CORS
CORS(app)

# Configurar el logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Inicializa la extensión SQLAlchemy
db.init_app(app)

# Inicializa Flask-Migrate
migrate = Migrate(app, db)

# Registrando blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(accesos_bp, url_prefix='/accesos')
app.register_blueprint(validate_bp)
app.register_blueprint(personas_bp, url_prefix='/personas')
app.register_blueprint(roles_bp)
app.register_blueprint(campus_bp)
app.register_blueprint(bloques_bp)
app.register_blueprint(aulas_bp)
app.register_blueprint(usuarios_bp, url_prefix='/usuarios')
app.register_blueprint(persona_rol_bp, url_prefix='/persona_rol')
app.register_blueprint(historial_bp)
app.register_blueprint(permisos_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
