from flask import Blueprint
from controllers.ambiente.aula_controller import AulaController


aulas_bp = Blueprint('aulas', __name__)

aulas_bp.route('/aulas', methods=['POST'])(AulaController.create_aula)
aulas_bp.route('/aulas', methods=['GET'])(AulaController.get_aulas)
aulas_bp.route('/aulas/<int:id>', methods=['GET'])(AulaController.get_aula)
aulas_bp.route('/aulas/<int:id>', methods=['PUT'])(AulaController.update_aula)
aulas_bp.route('/aulas/<int:id>', methods=['DELETE'])(AulaController.delete_aula)
