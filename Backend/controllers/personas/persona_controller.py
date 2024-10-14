from flask import jsonify, request
from services.personas.persona_service import PersonaService
from models import db, Persona  # Asegúrate de importar la clase Persona

class PersonaController:
    @staticmethod
    def create_persona():
        data = request.json
        required_fields = ['nombre', 'email', 'tarjeta_rfid', 'clave', 'nombre_usuario', 'password']

        # Validar que todos los campos requeridos están presentes
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Faltan campos requeridos'}), 400

        try:
            # Crear la nueva persona a través del servicio
            nueva_persona = PersonaService.create_persona(data)
            return jsonify({'message': 'Persona creada', 'id': nueva_persona.id}), 201
        except ValueError as e:
            return jsonify({'error': str(e)}), 400

    @staticmethod
    def get_personas():
        personas = PersonaService.get_personas()
        return jsonify([{
            'id': p.id,
            'nombre': p.nombre,
            'email': p.email,
            'tarjeta_rfid': p.tarjeta_rfid,
            'nombre_usuario': p.nombre_usuario
        } for p in personas])

    @staticmethod
    def get_persona(id):
        persona = PersonaService.get_persona(id)
        if persona:
            return jsonify({
                'id': persona.id,
                'nombre': persona.nombre,
                'email': persona.email,
                'tarjeta_rfid': persona.tarjeta_rfid,
                'nombre_usuario': persona.nombre_usuario,
                'clave': persona.clave
            })
        return jsonify({'message': 'Persona no encontrada'}), 404

    @staticmethod
    def update_persona(id):
        updated_persona = PersonaService.update_persona(id, request.json)
        if updated_persona:
            return jsonify({'message': 'Persona actualizada'})
        return jsonify({'message': 'Persona no encontrada'}), 404

    @staticmethod
    def delete_persona(id):
        if PersonaService.delete_persona(id):
            return jsonify({'message': 'Persona eliminada'})
        return jsonify({'message': 'Persona no encontrada'}), 404
