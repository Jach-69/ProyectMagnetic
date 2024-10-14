from models import HistorialAcceso

class HistorialService:
    @staticmethod
    def get_all_historial():
        historial = HistorialAcceso.query.all()
        return [
            {
                'id': h.id,
                'persona_id': h.persona_id,
                'aula_id': h.aula_id,
                'fecha_hora': h.fecha_hora,
                'es_valido': h.es_valido
            } for h in historial
        ]

    @staticmethod
    def get_historial_by_id(id):
        return HistorialAcceso.query.get(id)
