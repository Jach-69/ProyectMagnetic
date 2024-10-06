# routes/bloques.py
from flask import Blueprint, jsonify, request
from models import db, Bloque

bloques_bp = Blueprint('bloques', __name__)

@bloques_bp.route('/bloques', methods=['POST'])
def create_bloque():
    data = request.json
    nuevo_bloque = Bloque(**data)
    db.session.add(nuevo_bloque)
    db.session.commit()
    return jsonify({'message': 'Bloque creado', 'id': nuevo_bloque.id}), 201

@bloques_bp.route('/bloques', methods=['GET'])
def get_bloques():
    bloques = Bloque.query.all()
    return jsonify([{'id': b.id, 'nombre_bloque': b.nombre_bloque} for b in bloques])

@bloques_bp.route('/bloques/<int:id>', methods=['GET'])
def get_bloque(id):
    bloque = Bloque.query.get(id)
    if bloque:
        return jsonify({'id': bloque.id, 'nombre_bloque': bloque.nombre_bloque})
    return jsonify({'message': 'Bloque no encontrado'}), 404

@bloques_bp.route('/bloques/<int:id>', methods=['PUT'])
def update_bloque(id):
    bloque = Bloque.query.get(id)
    if bloque:
        data = request.json
        for key, value in data.items():
            setattr(bloque, key, value)
        db.session.commit()
        return jsonify({'message': 'Bloque actualizado'})
    return jsonify({'message': 'Bloque no encontrado'}), 404

@bloques_bp.route('/bloques/<int:id>', methods=['DELETE'])
def delete_bloque(id):
    bloque = Bloque.query.get(id)
    if bloque:
        db.session.delete(bloque)
        db.session.commit()
        return jsonify({'message': 'Bloque eliminado'})
    return jsonify({'message': 'Bloque no encontrado'}), 404
