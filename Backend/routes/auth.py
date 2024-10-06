from flask import Blueprint, request, jsonify
import psycopg2
from config import Config

auth_bp = Blueprint('auth', __name__)

# Conexión a la base de datos
conn = psycopg2.connect(Config.SQLALCHEMY_DATABASE_URI)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    nombre_usuario = data.get('nombre_usuario')
    password = data.get('password')

    if not nombre_usuario or not password:
        return jsonify({"status": "fail", "message": "Nombre de usuario y contraseña son requeridos"}), 400

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT password FROM personas WHERE nombre_usuario = %s", (nombre_usuario,))
            result = cursor.fetchone()
            if result and result[0] == password:  # Cambia esto por la comparación de hashes
                return jsonify({"status": "success", "message": "Login exitoso"}), 200
            else:
                return jsonify({"status": "fail", "message": "Nombre de usuario o contraseña incorrectos"}), 401
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
