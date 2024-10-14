from flask import Blueprint
from controllers.personas.roles_controller import RolesController

roles_bp = Blueprint('roles', __name__)

roles_bp.route('/roles', methods=['POST'])(RolesController.create_rol)
roles_bp.route('/roles', methods=['GET'])(RolesController.get_roles)
roles_bp.route('/roles/<int:id>', methods=['GET'])(RolesController.get_rol)
roles_bp.route('/roles/<int:id>', methods=['PUT'])(RolesController.update_rol)
roles_bp.route('/roles/<int:id>', methods=['DELETE'])(RolesController.delete_rol)
