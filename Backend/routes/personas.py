# routes/personas.py
from flask import Blueprint, jsonify, request
from models import db, Persona

personas_bp = Blueprint('personas', __name__)

@personas_bp.route('/personas', methods=['POST'])
def create_persona():
    data = request.json
    nueva_persona = Persona(**data)  # Asegúrate de que data contenga todos los campos requeridos
    db.session.add(nueva_persona)
    db.session.commit()
    return jsonify({'message': 'Persona creada', 'id': nueva_persona.id}), 201

@personas_bp.route('/personas', methods=['GET'])
def get_personas():
    personas = Persona.query.all()
    return jsonify([{
        'id': p.id,
        'nombre': p.nombre,
        'email': p.email,
        'tarjeta_rfid': p.tarjeta_rfid,
        'nombre_usuario': p.nombre_usuario
    } for p in personas])

@personas_bp.route('/personas/<int:id>', methods=['GET'])
def get_persona(id):
    persona = Persona.query.get(id)
    if persona:
        return jsonify({
            'id': persona.id,
            'nombre': persona.nombre,
            'email': persona.email,
            'tarjeta_rfid': persona.tarjeta_rfid,
            'nombre_usuario': persona.nombre_usuario
        })
    return jsonify({'message': 'Persona no encontrada'}), 404

@personas_bp.route('/personas/<int:id>', methods=['PUT'])
def update_persona(id):
    persona = Persona.query.get(id)
    if persona:
        data = request.json
        for key, value in data.items():
            setattr(persona, key, value)
        db.session.commit()
        return jsonify({'message': 'Persona actualizada'})
    return jsonify({'message': 'Persona no encontrada'}), 404

@personas_bp.route('/personas/<int:id>', methods=['DELETE'])
def delete_persona(id):
    persona = Persona.query.get(id)
    if persona:
        db.session.delete(persona)
        db.session.commit()
        return jsonify({'message': 'Persona eliminada'})
    return jsonify({'message': 'Persona no encontrada'}), 404
