# services/__init__.py
from .ambiente.campus_service import add_campus, get_all_campus, get_campus_by_id, update_campus_data, delete_campus_data
from .ambiente.bloque_service import BloqueService
from .ambiente.aula_service import AulaService
#from .personas.persona_service import PersonaService
#from .personas.rol_service import RolService
#from .personas.persona_rol_service import PersonaRolService
#from .personas.usuario_service import UsuarioService
#from .accesos.acceso_service import AccesoService
#from .accesos.historial_service import HistorialService
#from .permisos.permiso_service import PermisoService
