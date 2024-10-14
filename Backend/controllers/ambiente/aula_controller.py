from flask import jsonify, request
from services.ambiente.aula_service import AulaService

class AulaController:
    @staticmethod
    def create_aula():
        data = request.json
        if 'nombre_aula' not in data or 'bloque_id' not in data:
            return jsonify({'message': 'nombre_aula y bloque_id son requeridos'}), 400
        nueva_aula = AulaService.create_aula(data)
        return jsonify({'message': 'Aula creada', 'id': nueva_aula.id}), 201

    @staticmethod
    def get_aulas():
        aulas = AulaService.get_aulas()
        return jsonify([{
            'id': a.id,
            'nombre_aula': a.nombre_aula,
            'bloque_id': a.bloque_id
        } for a in aulas])

    @staticmethod
    def get_aula(id):
        aula = AulaService.get_aula(id)
        if aula:
            return jsonify({
                'id': aula.id,
                'nombre_aula': aula.nombre_aula,
                'bloque_id': aula.bloque_id
            })
        return jsonify({'message': 'Aula no encontrada'}), 404

    @staticmethod
    def update_aula(id):
        data = request.json
        updated_aula = AulaService.update_aula(id, data)
        if updated_aula:
            return jsonify({'message': 'Aula actualizada'})
        return jsonify({'message': 'Aula no encontrada'}), 404

    @staticmethod
    def delete_aula(id):
        if AulaService.delete_aula(id):
            return jsonify({'message': 'Aula eliminada'})
        return jsonify({'message': 'Aula no encontrada'}), 404
