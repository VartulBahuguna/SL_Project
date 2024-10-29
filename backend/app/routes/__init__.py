from .auth_routes import auth_blueprint
from .doctor_routes import doctor_blueprint
from .patient_routes import patient_blueprint
from .analysis_routes import analysis_blueprint
from .admin_routes import admin_blueprint

__all__ = ['auth_blueprint', 'doctor_blueprint', 'patient_blueprint', 'analysis_blueprint', 'admin_blueprint']
