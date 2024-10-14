from flask import jsonify, request
from services.ambiente.bloque_service import BloqueService  # Corrige la ruta

class BloqueController:
    @staticmethod
    def create_bloque():
        data = request.json
        if 'nombre_bloque' not in data or 'campus_id' not in data:
            return jsonify({'message': 'nombre_bloque y campus_id son requeridos'}), 400
        nuevo_bloque = BloqueService.create_bloque(data)
        return jsonify({'message': 'Bloque creado', 'id': nuevo_bloque.id}), 201

    @staticmethod
    def get_bloques():
        bloques = BloqueService.get_bloques()
        return jsonify(bloques)

    @staticmethod
    def get_bloque(id):
        bloque = BloqueService.get_bloque(id)
        if bloque:
            return jsonify(bloque)
        return jsonify({'message': 'Bloque no encontrado'}), 404

    @staticmethod
    def update_bloque(id):
        data = request.json
        updated_bloque = BloqueService.update_bloque(id, data)
        if updated_bloque:
            return jsonify({'message': 'Bloque actualizado'})
        return jsonify({'message': 'Bloque no encontrado'}), 404

    @staticmethod
    def delete_bloque(id):
        if BloqueService.delete_bloque(id):
            return jsonify({'message': 'Bloque eliminado'})
        return jsonify({'message': 'Bloque no encontrado'}), 404
