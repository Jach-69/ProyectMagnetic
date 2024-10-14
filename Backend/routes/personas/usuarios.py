from flask import Blueprint
from controllers.personas.usuarios_controller import UsuariosController

usuarios_bp = Blueprint('usuarios', __name__)

# Aquí no necesitas agregar '/usuarios' porque ya está en el url_prefix
usuarios_bp.route('/', methods=['POST'])(UsuariosController.create_usuario)
usuarios_bp.route('/', methods=['GET'])(UsuariosController.get_usuarios)
usuarios_bp.route('/<int:id>', methods=['GET'])(UsuariosController.get_usuario)
usuarios_bp.route('/<int:id>', methods=['PUT'])(UsuariosController.update_usuario)
usuarios_bp.route('/<int:id>', methods=['DELETE'])(UsuariosController.delete_usuario)
