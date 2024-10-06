from flask import Blueprint, jsonify, request
from models import db, Usuario, Acceso, HistorialAcceso
from sqlalchemy import text

validate_bp = Blueprint('validate', __name__)

@validate_bp.route('/validate', methods=['POST'])
def validate():
    data = request.json
    clave = data.get('clave')
    rfid = data.get('rfid')
    aula_id = data.get('aula_id')

    # Validación de entrada
    if not clave and not rfid:
        return jsonify({"status": "fail", "message": "Debe proporcionar al menos una clave o un RFID"}), 400

    # Construcción de la consulta
    query = text("""
    SELECT u.id AS usuario_id
    FROM usuarios u
    JOIN personas p ON u.persona_id = p.id
    WHERE 1=1
    """)

    if clave:
        query = text(query.text + " AND p.clave = :clave")
    if rfid:
        query = text(query.text + " AND p.tarjeta_rfid = :rfid")

    try:
        # Ejecutar la consulta
        params = {'clave': clave, 'rfid': rfid}
        usuario = db.session.execute(query, params).fetchone()

        if usuario:
            usuario_id = usuario[0]
            es_valido = True
        else:
            usuario_id = None
            es_valido = False

        # Crear un nuevo registro en accesos
        nuevo_acceso = Acceso(es_valido=es_valido, usuario_id=usuario_id, aula_id=aula_id)
        db.session.add(nuevo_acceso)

        # Solo registrar en el historial si el usuario es válido
        if usuario_id is not None:
            nuevo_historial = HistorialAcceso(usuario_id=usuario_id, aula_id=aula_id, es_valido=es_valido)
            db.session.add(nuevo_historial)

        # Commit una sola vez
        db.session.commit()

        message = "Access granted" if es_valido else "Access denied"
        return jsonify({"status": "success", "message": message}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500
