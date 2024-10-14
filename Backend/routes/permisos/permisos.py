from flask import Blueprint
from controllers.permisos.permiso_controller import PermisoController

permisos_bp = Blueprint('permisos', __name__)

@permisos_bp.route('/permisos', methods=['POST'])
def create_permiso():
    return PermisoController.create_permiso()

@permisos_bp.route('/permisos', methods=['GET'])
def get_permisos():
    return PermisoController.get_permisos()

@permisos_bp.route('/permisos/<int:id>', methods=['GET'])
def get_permiso(id):
    return PermisoController.get_permiso(id)

@permisos_bp.route('/permisos/<int:id>', methods=['PUT'])
def update_permiso(id):
    return PermisoController.update_permiso(id)

@permisos_bp.route('/permisos/<int:id>', methods=['DELETE'])
def delete_permiso(id):
    return PermisoController.delete_permiso(id)
