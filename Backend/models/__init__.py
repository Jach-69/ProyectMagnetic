from flask_sqlalchemy import SQLAlchemy

# Inicializa la instancia de SQLAlchemy
db = SQLAlchemy()

# Importar los modelos para asegurarte de que se registren con SQLAlchemy
from .ambiente.campus import Campus
from .ambiente.bloque import Bloque
from .ambiente.aula import Aula
from .personas.persona import Persona
from .personas.rol import Rol
from .personas.persona_rol import PersonaRol
from .personas.usuario import Usuario
from .accesos.acceso import Acceso
from .accesos.historial import HistorialAcceso
from .permisos.permiso import PermisoAcceso
