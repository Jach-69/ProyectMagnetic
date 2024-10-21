from flask import Blueprint

# Inicialización de los blueprints
def register_routes(app):
    from .auth import auth_bp
    from .accesos.acceso import accesos_bp
    from .validate import validate_bp
    from .personas import personas_bp  # Asegúrate de importar personas_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(accesos_bp)
    app.register_blueprint(validate_bp)
    app.register_blueprint(personas_bp)  # Registra el blueprint de personas
