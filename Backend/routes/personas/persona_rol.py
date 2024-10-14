from flask import Blueprint, jsonify, request
from services.personas.persona_rol_service import PersonaRolService

persona_rol_bp = Blueprint('persona_rol', __name__)

@persona_rol_bp.route('/', methods=['POST'])
def create_persona_rol():
    data = request.json
    nuevo_persona_rol = PersonaRolService.create_persona_rol(data)
    return jsonify({'message': 'Relación Persona-Rol creada', 'id': nuevo_persona_rol.id}), 201

@persona_rol_bp.route('/', methods=['GET'])
def get_persona_roles():
    persona_roles = PersonaRolService.get_persona_roles()
    return jsonify([{'id': pr.id, 'persona_id': pr.persona_id, 'rol_id': pr.rol_id} for pr in persona_roles])

@persona_rol_bp.route('/<int:id>', methods=['GET'])
def get_persona_rol(id):
    persona_rol = PersonaRolService.get_persona_rol(id)
    if persona_rol:
        return jsonify({'id': persona_rol.id, 'persona_id': persona_rol.persona_id, 'rol_id': persona_rol.rol_id})
    return jsonify({'message': 'Relación Persona-Rol no encontrada'}), 404

@persona_rol_bp.route('/<int:id>', methods=['PUT'])
def update_persona_rol(id):
    data = request.json
    persona_rol = PersonaRolService.update_persona_rol(id, data)
    if persona_rol:
        return jsonify({'message': 'Relación Persona-Rol actualizada'})
    return jsonify({'message': 'Relación Persona-Rol no encontrada'}), 404

@persona_rol_bp.route('/<int:id>', methods=['DELETE'])
def delete_persona_rol(id):
    if PersonaRolService.delete_persona_rol(id):
        return jsonify({'message': 'Relación Persona-Rol eliminada'})
    return jsonify({'message': 'Relación Persona-Rol no encontrada'}), 404
