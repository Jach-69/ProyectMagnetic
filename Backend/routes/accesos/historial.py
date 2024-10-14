from flask import Blueprint
from controllers.accesos.historial_controller import HistorialController

historial_bp = Blueprint('historial', __name__)

@historial_bp.route('/historial', methods=['GET'])
def get_historial():
    return HistorialController.get_historial()

@historial_bp.route('/historial/<int:id>', methods=['GET'])
def get_historial_acceso(id):
    return HistorialController.get_historial_acceso(id)
