from flask import jsonify, request
from models import db, PermisoAcceso

class PermisoController:

    @staticmethod
    def create_permiso():
        data = request.json
        nuevo_permiso = PermisoAcceso(**data)  # Asegúrate de que data tenga 'persona_id' y 'aula_id'
        db.session.add(nuevo_permiso)
        db.session.commit()
        return jsonify({'message': 'Permiso de acceso creado', 'id': nuevo_permiso.id}), 201

    @staticmethod
    def get_permisos():
        permisos = PermisoAcceso.query.all()
        return jsonify([{'id': p.id, 'persona_id': p.persona_id, 'aula_id': p.aula_id, 'es_universal': p.es_universal} for p in permisos])

    @staticmethod
    def get_permiso(id):
        permiso = PermisoAcceso.query.get(id)
        if permiso:
            return jsonify({'id': permiso.id, 'persona_id': permiso.persona_id, 'aula_id': permiso.aula_id, 'es_universal': permiso.es_universal})
        return jsonify({'message': 'Permiso de acceso no encontrado'}), 404

    @staticmethod
    def update_permiso(id):
        data = request.json
        permiso = PermisoAcceso.query.get(id)

        if permiso:
            permiso.persona_id = data.get('persona_id', permiso.persona_id)
            permiso.aula_id = data.get('aula_id', permiso.aula_id)
            permiso.es_universal = data.get('es_universal', permiso.es_universal)
            db.session.commit()
            return jsonify({'message': 'Permiso de acceso actualizado', 'id': permiso.id})

        return jsonify({'message': 'Permiso de acceso no encontrado'}), 404

    @staticmethod
    def delete_permiso(id):
        permiso = PermisoAcceso.query.get(id)
        if permiso:
            db.session.delete(permiso)
            db.session.commit()
            return jsonify({'message': 'Permiso de acceso eliminado'})
        return jsonify({'message': 'Permiso de acceso no encontrado'}), 404
