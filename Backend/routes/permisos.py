from flask import Blueprint, jsonify, request
from models import db, PermisoAcceso

permisos_bp = Blueprint('permisos', __name__)

@permisos_bp.route('/permisos', methods=['POST'])
def create_permiso():
    data = request.json
    nuevo_permiso = PermisoAcceso(**data)  # Asume que data tiene los campos correctos
    db.session.add(nuevo_permiso)
    db.session.commit()
    return jsonify({'message': 'Permiso de acceso creado', 'id': nuevo_permiso.id}), 201

@permisos_bp.route('/permisos', methods=['GET'])
def get_permisos():
    permisos = PermisoAcceso.query.all()
    return jsonify([{'id': p.id, 'usuario_id': p.usuario_id, 'aula_id': p.aula_id} for p in permisos])

@permisos_bp.route('/permisos/<int:id>', methods=['GET'])
def get_permiso(id):
    permiso = PermisoAcceso.query.get(id)
    if permiso:
        return jsonify({'id': permiso.id, 'usuario_id': permiso.usuario_id, 'aula_id': permiso.aula_id})
    return jsonify({'message': 'Permiso de acceso no encontrado'}), 404

@permisos_bp.route('/permisos/<int:id>', methods=['PUT'])
def update_permiso(id):
    data = request.json
    permiso = PermisoAcceso.query.get(id)
    
    if permiso:
        # Actualiza los campos del permiso con los nuevos datos
        permiso.usuario_id = data.get('usuario_id', permiso.usuario_id)
        permiso.aula_id = data.get('aula_id', permiso.aula_id)
        
        db.session.commit()
        return jsonify({'message': 'Permiso de acceso actualizado', 'id': permiso.id})
    
    return jsonify({'message': 'Permiso de acceso no encontrado'}), 404


@permisos_bp.route('/permisos/<int:id>', methods=['DELETE'])
def delete_permiso(id):
    permiso = PermisoAcceso.query.get(id)
    if permiso:
        db.session.delete(permiso)
        db.session.commit()
        return jsonify({'message': 'Permiso de acceso eliminado'})
    return jsonify({'message': 'Permiso de acceso no encontrado'}), 404
