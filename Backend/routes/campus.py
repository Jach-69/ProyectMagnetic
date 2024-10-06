# routes/campus.py
from flask import Blueprint, jsonify, request
from models import db, Campus

campus_bp = Blueprint('campus', __name__)

@campus_bp.route('/campus', methods=['POST'])
def create_campus():
    data = request.json
    nuevo_campus = Campus(**data)
    db.session.add(nuevo_campus)
    db.session.commit()
    return jsonify({'message': 'Campus creado', 'id': nuevo_campus.id}), 201

@campus_bp.route('/campus', methods=['GET'])
def get_campus():
    campus = Campus.query.all()
    return jsonify([{'id': c.id, 'nombre_campus': c.nombre_campus} for c in campus])

@campus_bp.route('/campus/<int:id>', methods=['GET'])
def get_campus_by_id(id):
    campus = Campus.query.get(id)
    if campus:
        return jsonify({'id': campus.id, 'nombre_campus': campus.nombre_campus})
    return jsonify({'message': 'Campus no encontrado'}), 404

@campus_bp.route('/campus/<int:id>', methods=['PUT'])
def update_campus(id):
    campus = Campus.query.get(id)
    if campus:
        data = request.json
        for key, value in data.items():
            setattr(campus, key, value)
        db.session.commit()
        return jsonify({'message': 'Campus actualizado'})
    return jsonify({'message': 'Campus no encontrado'}), 404

@campus_bp.route('/campus/<int:id>', methods=['DELETE'])
def delete_campus(id):
    campus = Campus.query.get(id)
    if campus:
        db.session.delete(campus)
        db.session.commit()
        return jsonify({'message': 'Campus eliminado'})
    return jsonify({'message': 'Campus no encontrado'}), 404
