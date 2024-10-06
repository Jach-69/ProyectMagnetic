from flask import Blueprint, jsonify, request
from models import db, Usuario

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.json
    nuevo_usuario = Usuario(**data)  # Asume que data tiene los campos correctos
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'message': 'Usuario creado', 'id': nuevo_usuario.id}), 201

@usuarios_bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{'id': u.id, 'persona_id': u.persona_id, 'rol_id': u.rol_id} for u in usuarios])

@usuarios_bp.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        return jsonify({'id': usuario.id, 'persona_id': usuario.persona_id, 'rol_id': usuario.rol_id})
    return jsonify({'message': 'Usuario no encontrado'}), 404

@usuarios_bp.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        data = request.json
        for key, value in data.items():
            setattr(usuario, key, value)
        db.session.commit()
        return jsonify({'message': 'Usuario actualizado'})
    return jsonify({'message': 'Usuario no encontrado'}), 404

@usuarios_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({'message': 'Usuario eliminado'})
    return jsonify({'message': 'Usuario no encontrado'}), 404
