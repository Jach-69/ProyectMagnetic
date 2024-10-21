from flask import jsonify, request
from services.personas.rol_service import RolService

class RolesController:
    @staticmethod
    def create_rol():
        data = request.json
        if not data or 'nombre_rol' not in data:
            return jsonify({'message': 'Datos inválidos'}), 400
        nuevo_rol = RolService.create_rol(data)
        return jsonify({'message': 'Rol creado', 'id': nuevo_rol.id}), 201

    @staticmethod
    def get_roles():
        roles = RolService.get_roles()
        return jsonify([{'id': r.id, 'nombre_rol': r.nombre_rol} for r in roles])

    @staticmethod
    def get_rol(id):
        rol = RolService.get_rol(id)
        if rol:
            return jsonify({'id': rol.id, 'nombre_rol': rol.nombre_rol})
        return jsonify({'message': 'Rol no encontrado'}), 404

    @staticmethod
    def update_rol(id):
        updated_rol = RolService.update_rol(id, request.json)
        if updated_rol:
            return jsonify({'message': 'Rol actualizado'})
        return jsonify({'message': 'Rol no encontrado'}), 404

    @staticmethod
    def delete_rol(id):
        if RolService.delete_rol(id):
            return jsonify({'message': 'Rol eliminado'})
        return jsonify({'message': 'Rol no encontrado'}), 404
