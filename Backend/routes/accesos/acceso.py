from flask import Blueprint
from controllers.accesos.acceso_controller import AccesosController

accesos_bp = Blueprint('accesos', __name__)

# Rutas del blueprint
accesos_bp.route('/', methods=['GET'])(AccesosController.get_accesos)
accesos_bp.route('/<int:id>', methods=['GET'])(AccesosController.get_acceso)
accesos_bp.route('/', methods=['POST'])(AccesosController.create_acceso)
accesos_bp.route('/<int:id>', methods=['DELETE'])(AccesosController.delete_acceso)
