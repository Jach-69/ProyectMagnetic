from flask import Blueprint, jsonify
from models import db, HistorialAcceso

historial_bp = Blueprint('historial', __name__)

@historial_bp.route('/historial', methods=['GET'])
def get_historial():
    historial = HistorialAcceso.query.all()
    return jsonify([{'id': h.id, 'usuario_id': h.usuario_id, 'aula_id': h.aula_id, 'fecha_hora': h.fecha_hora, 'es_valido': h.es_valido} for h in historial])

@historial_bp.route('/historial/<int:id>', methods=['GET'])
def get_historial_acceso(id):
    historial = HistorialAcceso.query.get(id)
    if historial:
        return jsonify({'id': historial.id, 'usuario_id': historial.usuario_id, 'aula_id': historial.aula_id, 'fecha_hora': historial.fecha_hora, 'es_valido': historial.es_valido})
    return jsonify({'message': 'Historial de acceso no encontrado'}), 404
