from flask import Flask, jsonify
from elasticapm.contrib.flask import ElasticAPM
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from config import Config
import os
import elasticapm

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
csrf = CSRFProtect()
apm = ElasticAPM()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Create upload directory if it doesn't exist
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # Initialize APM
    app.config['ELASTIC_APM'] = {
        'SERVICE_NAME': 'health-api',
        'SERVER_URL': 'http://localhost:8200',
        'ENVIRONMENT': 'production',
    }
    apm.init_app(app)

    # Initialize database and extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    csrf.init_app(app)

    # Set security headers
    @app.after_request
    def set_security_headers(response):
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['Content-Security-Policy'] = "default-src 'self';"
        return response

    # Set up rate limiting
    limiter = Limiter(
        key_func=get_remote_address,
        app=app,
        default_limits=["200 per day", "50 per hour"]
    )
    from .routes import auth_blueprint, doctor_blueprint, patient_blueprint, analysis_blueprint, admin_blueprint
    # Register blueprints
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(doctor_blueprint)
    app.register_blueprint(patient_blueprint)
    app.register_blueprint(analysis_blueprint)
    app.register_blueprint(admin_blueprint)

    # Global error handler
    @app.errorhandler(Exception)
    def handle_exception(e):
        if apm:
            apm.capture_exception()
        return jsonify({'message': 'An unexpected error occurred', 'error': str(e)}), 500

    return app
