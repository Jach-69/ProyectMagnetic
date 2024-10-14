from flask import jsonify
from services.accesos.historial_service import HistorialService

class HistorialController:
    @staticmethod
    def get_historial():
        historial = HistorialService.get_all_historial()
        return jsonify(historial)

    @staticmethod
    def get_historial_acceso(id):
        historial = HistorialService.get_historial_by_id(id)
        if historial:
            return jsonify({
                'id': historial.id,
                'persona_id': historial.persona_id,
                'aula_id': historial.aula_id,
                'fecha_hora': historial.fecha_hora,
                'es_valido': historial.es_valido
            })
        return jsonify({'message': 'Historial de acceso no encontrado'}), 404
