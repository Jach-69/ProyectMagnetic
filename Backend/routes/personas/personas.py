from flask import Blueprint
from controllers.personas.persona_controller import PersonaController

personas_bp = Blueprint('personas', __name__)

# Rutas del blueprint
personas_bp.route('/', methods=['POST'])(PersonaController.create_persona)
personas_bp.route('/', methods=['GET'])(PersonaController.get_personas)
personas_bp.route('/<int:id>', methods=['GET'])(PersonaController.get_persona)
personas_bp.route('/<int:id>', methods=['PUT'])(PersonaController.update_persona)
personas_bp.route('/<int:id>', methods=['DELETE'])(PersonaController.delete_persona)
