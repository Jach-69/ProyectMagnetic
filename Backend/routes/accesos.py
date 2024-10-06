from flask import Blueprint, jsonify, request
from models import db, Acceso

accesos_bp = Blueprint('accesos', __name__)

@accesos_bp.route('/accesos', methods=['GET'])
def get_accesos():
    accesos = Acceso.query.all()
    return jsonify([{'id': a.id, 'fecha_hora': a.fecha_hora, 'es_valido': a.es_valido, 'usuario_id': a.usuario_id, 'aula_id': a.aula_id} for a in accesos])

@accesos_bp.route('/accesos/<int:id>', methods=['GET'])
def get_acceso(id):
    acceso = Acceso.query.get(id)
    if acceso:
        return jsonify({'id': acceso.id, 'fecha_hora': acceso.fecha_hora, 'es_valido': acceso.es_valido, 'usuario_id': acceso.usuario_id, 'aula_id': acceso.aula_id})
    return jsonify({'message': 'Acceso no encontrado'}), 404

@accesos_bp.route('/accesos/<int:id>', methods=['DELETE'])
def delete_acceso(id):
    acceso = Acceso.query.get(id)
    if acceso:
        db.session.delete(acceso)
        db.session.commit()
        return jsonify({'message': 'Acceso eliminado'})
    return jsonify({'message': 'Acceso no encontrado'}), 404
