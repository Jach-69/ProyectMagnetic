# routes/aulas.py
from flask import Blueprint, jsonify, request
from models import db, Aula

aulas_bp = Blueprint('aulas', __name__)

@aulas_bp.route('/aulas', methods=['POST'])
def create_aula():
    data = request.json
    nueva_aula = Aula(**data)  # Se espera que 'data' incluya 'bloque_id'
    db.session.add(nueva_aula)
    db.session.commit()
    return jsonify({'message': 'Aula creada', 'id': nueva_aula.id}), 201

@aulas_bp.route('/aulas', methods=['GET'])
def get_aulas():
    aulas = Aula.query.all()
    # Incluye 'bloque_id' en la respuesta
    return jsonify([
        {
            'id': a.id,
            'nombre_aula': a.nombre_aula,
            'bloque_id': a.bloque_id  # Incluir bloque_id
        }
        for a in aulas
    ])

@aulas_bp.route('/aulas/<int:id>', methods=['GET'])
def get_aula(id):
    aula = Aula.query.get(id)
    if aula:
        return jsonify({
            'id': aula.id,
            'nombre_aula': aula.nombre_aula,
            'bloque_id': aula.bloque_id  # Incluir bloque_id
        })
    return jsonify({'message': 'Aula no encontrada'}), 404

@aulas_bp.route('/aulas/<int:id>', methods=['PUT'])
def update_aula(id):
    aula = Aula.query.get(id)
    if aula:
        data = request.json
        for key, value in data.items():
            setattr(aula, key, value)
        db.session.commit()
        return jsonify({'message': 'Aula actualizada'})
    return jsonify({'message': 'Aula no encontrada'}), 404

@aulas_bp.route('/aulas/<int:id>', methods=['DELETE'])
def delete_aula(id):
    aula = Aula.query.get(id)
    if aula:
        db.session.delete(aula)
        db.session.commit()
        return jsonify({'message': 'Aula eliminada'})
    return jsonify({'message': 'Aula no encontrada'}), 404
