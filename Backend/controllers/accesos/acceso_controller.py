from flask import jsonify, request
from services.accesos.acceso_service import AccesosService

class AccesosController:
    @staticmethod
    def get_accesos():
        accesos = AccesosService.get_all_accesos()
        return jsonify(accesos), 200

    @staticmethod
    def get_acceso(id):
        acceso = AccesosService.get_acceso_by_id(id)
        if acceso:
            return jsonify(acceso), 200
        return jsonify({'message': 'Acceso no encontrado'}), 404

    @staticmethod
    def create_acceso():
        data = request.json
        nuevo_acceso = AccesosService.create_acceso(data)
        return jsonify({'message': 'Acceso creado', 'id': nuevo_acceso.id}), 201

    @staticmethod
    def delete_acceso(id):
        if AccesosService.delete_acceso(id):
            return jsonify({'message': 'Acceso eliminado'}), 200
        return jsonify({'message': 'Acceso no encontrado'}), 404
