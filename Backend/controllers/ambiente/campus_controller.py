# controllers/ambiente/campus_controller.py
from flask import jsonify, request
from services.ambiente.campus_service import (
    add_campus,
    get_all_campus,
    get_campus_by_id,
    update_campus_data,
    delete_campus_data
)

class CampusController:
    @staticmethod
    def create_campus():
        data = request.json
        nuevo_campus = add_campus(data)
        return jsonify({'message': 'Campus creado', 'id': nuevo_campus.id}), 201

    @staticmethod
    def get_campus():
        campus = get_all_campus()
        return jsonify([{'id': c.id, 'nombre_campus': c.nombre_campus} for c in campus])

    @staticmethod
    def get_campus_by_id(id):
        campus = get_campus_by_id(id)
        if campus:
            return jsonify({'id': campus.id, 'nombre_campus': campus.nombre_campus})
        return jsonify({'message': 'Campus no encontrado'}), 404

    @staticmethod
    def update_campus(id):
        campus = update_campus_data(id, request.json)
        if campus:
            return jsonify({'message': 'Campus actualizado'})
        return jsonify({'message': 'Campus no encontrado'}), 404

    @staticmethod
    def delete_campus(id):
        campus = delete_campus_data(id)
        if campus:
            return jsonify({'message': 'Campus eliminado'})
        return jsonify({'message': 'Campus no encontrado'}), 404
