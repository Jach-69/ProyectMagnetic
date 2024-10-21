from flask import Blueprint, jsonify, request
from models import db, Usuario, Acceso, HistorialAcceso, PermisoAcceso
from sqlalchemy import text

validate_bp = Blueprint('validate', __name__)

def is_user_allowed(usuario_id, aula_id):
    # Verificar si el usuario existe y obtener el rol
    usuario = Usuario.query.filter_by(id=usuario_id).first()
    
    if usuario is None:
        return False  # Si el usuario no existe, se deniega el acceso
    
    # Verificar si el usuario es un administrador
    if usuario.rol_id == 1:  # Suponiendo que 1 es el ID del rol de administrador
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

    # Debugging: Print values to verify input
    print(f"Clave: {clave}, RFID: {rfid}, Aula ID: {aula_id}")

    # Convert empty strings to None
    if clave == '':
        clave = None
    if rfid == '':
        rfid = None

    if not clave and not rfid:
        return jsonify({"status": "fail", "message": "Debe proporcionar al menos una clave o un RFID"}), 400

    # Query construction
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
        # Initializing parameters
        params = {'clave': clave, 'rfid': rfid}
        
        # Debugging: Print final query and params
        print(f"Executing query: {query}, Params: {params}")

        # Execute the query
        usuario = db.session.execute(query, params).fetchone()

        if not usuario:
            return jsonify({"status": "fail", "message": "Usuario no encontrado"}), 401
        
        # Proceed with access check
        usuario_id = usuario[0]
        persona_id = usuario[1]
        
        # Verify if user is allowed in the aula
        if not is_user_allowed(persona_id, aula_id):
            # If not allowed, return access denied
            return jsonify({"status": "fail", "message": "Acceso denegado para el aula especificada"}), 401

        # If user is allowed, insert access record
        nuevo_acceso = Acceso(es_valido=True, usuario_id=usuario_id, aula_id=aula_id)
        db.session.add(nuevo_acceso)

        # Insert a record in the history
        nuevo_historial = HistorialAcceso(persona_id=persona_id, aula_id=aula_id, es_valido=True)
        db.session.add(nuevo_historial)

        db.session.commit()

        return jsonify({"status": "success", "message": "Acceso concedido"}), 200

    except Exception as e:
        # Detailed error log for debugging
        print(f"Error: {str(e)}")
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500
