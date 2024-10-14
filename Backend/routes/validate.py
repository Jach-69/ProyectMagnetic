from flask import Blueprint, jsonify, request
from models import db, Usuario, Acceso, HistorialAcceso, PermisoAcceso  # Asegúrate de importar PermisoAcceso
from sqlalchemy import text

validate_bp = Blueprint('validate', __name__)

def is_user_allowed(usuario_id, aula_id):
    # Verificar si el usuario es un administrador
    rol_id = Usuario.query.filter_by(id=usuario_id).first().rol_id
    if rol_id == 1:  # Suponiendo que 1 es el ID del rol de administrador
        return True  # Acceso universal otorgado

    # Verificar si el usuario tiene acceso universal
    permiso_universal = PermisoAcceso.query.filter_by(persona_id=usuario_id, es_universal=True).first()
    if permiso_universal:
        return True  # Acceso universal otorgado

    # Verificar si el usuario tiene permiso específico para acceder a la aula
    permiso_especifico = PermisoAcceso.query.filter_by(persona_id=usuario_id, aula_id=aula_id).first()
    return permiso_especifico is not None

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
    SELECT u.id AS usuario_id, p.id AS persona_id
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

        if not usuario:
            return jsonify({"status": "fail", "message": "Usuario no encontrado"}), 401
        
        usuario_id = usuario[0]
        persona_id = usuario[1]  # Captura el persona_id
        es_valido = True

        # Verificar si el usuario tiene permiso para acceder al aula
        if not is_user_allowed(persona_id, aula_id):
            es_valido = False  # Denegar acceso si no está en la whitelist

        # Crear un nuevo registro en accesos
        nuevo_acceso = Acceso(es_valido=es_valido, usuario_id=usuario_id, aula_id=aula_id)
        db.session.add(nuevo_acceso)

        # Solo registrar en el historial si el usuario es válido
        if usuario_id is not None:
            nuevo_historial = HistorialAcceso(persona_id=persona_id, aula_id=aula_id, es_valido=es_valido)
            db.session.add(nuevo_historial)

        # Commit una sola vez
        db.session.commit()

        message = "Access granted" if es_valido else "Access denied"
        return jsonify({"status": "success", "message": message}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500
