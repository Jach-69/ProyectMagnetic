from flask import Blueprint
from controllers.ambiente.bloque_controller import BloqueController


bloques_bp = Blueprint('bloques', __name__)

bloques_bp.route('/bloques', methods=['POST'])(BloqueController.create_bloque)
bloques_bp.route('/bloques', methods=['GET'])(BloqueController.get_bloques)
bloques_bp.route('/bloques/<int:id>', methods=['GET'])(BloqueController.get_bloque)
bloques_bp.route('/bloques/<int:id>', methods=['PUT'])(BloqueController.update_bloque)
bloques_bp.route('/bloques/<int:id>', methods=['DELETE'])(BloqueController.delete_bloque)
