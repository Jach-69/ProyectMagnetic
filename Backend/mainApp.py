from flask import Flask
from flask_cors import CORS
from config import Config
from models import db  # Importa el objeto db


from routes.auth import auth_bp
from routes.accesos import accesos_bp
from routes.validate import validate_bp  # Asegúrate de importar también el blueprint de validate

from routes.personas import personas_bp
from routes.roles import roles_bp
from routes.campus import campus_bp
from routes.bloques import bloques_bp
from routes.aulas import aulas_bp

from routes.usuarios import usuarios_bp
from routes.historial import historial_bp
from routes.permisos import permisos_bp


app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Inicializa la extensión SQLAlchemy
db.init_app(app)

# Registrando blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(accesos_bp)
app.register_blueprint(validate_bp)  # Registra el blueprint de validate
app.register_blueprint(personas_bp)
app.register_blueprint(roles_bp)
app.register_blueprint(campus_bp)
app.register_blueprint(bloques_bp)
app.register_blueprint(aulas_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(historial_bp)
app.register_blueprint(permisos_bp)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
