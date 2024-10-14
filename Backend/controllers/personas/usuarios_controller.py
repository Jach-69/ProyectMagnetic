from flask import jsonify, request
from services.personas.usuario_service import UsuarioService

class UsuariosController:
    @staticmethod
    def create_usuario():
        data = request.json
        nuevo_usuario = UsuarioService.create_usuario(data)
        return jsonify({'message': 'Usuario creado', 'id': nuevo_usuario.id}), 201

    @staticmethod
    def get_usuarios():
        usuarios = UsuarioService.get_usuarios()
        return jsonify([{'id': u.id, 'persona_id': u.persona_id, 'rol_id': u.rol_id} for u in usuarios])

    @staticmethod
    def get_usuario(id):
        usuario = UsuarioService.get_usuario(id)
        if usuario:
            return jsonify({'id': usuario.id, 'persona_id': usuario.persona_id, 'rol_id': usuario.rol_id})
        return jsonify({'message': 'Usuario no encontrado'}), 404

    @staticmethod
    def update_usuario(id):
        updated_usuario = UsuarioService.update_usuario(id, request.json)
        if updated_usuario:
            return jsonify({'message': 'Usuario actualizado'})
        return jsonify({'message': 'Usuario no encontrado'}), 404

    @staticmethod
    def delete_usuario(id):
        if UsuarioService.delete_usuario(id):
            return jsonify({'message': 'Usuario eliminado'})
        return jsonify({'message': 'Usuario no encontrado'}), 404
