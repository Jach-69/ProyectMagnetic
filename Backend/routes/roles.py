# routes/roles.py
from flask import Blueprint, jsonify, request
from models import db, Rol

roles_bp = Blueprint('roles', __name__)

@roles_bp.route('/roles', methods=['POST'])
def create_rol():
    data = request.json
    nuevo_rol = Rol(**data)
    db.session.add(nuevo_rol)
    db.session.commit()
    return jsonify({'message': 'Rol creado', 'id': nuevo_rol.id}), 201

@roles_bp.route('/roles', methods=['GET'])
def get_roles():
    roles = Rol.query.all()
    return jsonify([{'id': r.id, 'nombre_rol': r.nombre_rol} for r in roles])

@roles_bp.route('/roles/<int:id>', methods=['GET'])
def get_rol(id):
    rol = Rol.query.get(id)
    if rol:
        return jsonify({'id': rol.id, 'nombre_rol': rol.nombre_rol})
    return jsonify({'message': 'Rol no encontrado'}), 404

@roles_bp.route('/roles/<int:id>', methods=['PUT'])
def update_rol(id):
    rol = Rol.query.get(id)
    if rol:
        data = request.json
        for key, value in data.items():
            setattr(rol, key, value)
        db.session.commit()
        return jsonify({'message': 'Rol actualizado'})
    return jsonify({'message': 'Rol no encontrado'}), 404

@roles_bp.route('/roles/<int:id>', methods=['DELETE'])
def delete_rol(id):
    rol = Rol.query.get(id)
    if rol:
        db.session.delete(rol)
        db.session.commit()
        return jsonify({'message': 'Rol eliminado'})
    return jsonify({'message': 'Rol no encontrado'}), 404
