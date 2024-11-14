from flask import Blueprint, request, jsonify
from app.models import Patient, db
from .. import bcrypt, jwt
from flask_jwt_extended import create_access_token
from elasticapm import capture_span
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from datetime import datetime

patient_auth_blueprint = Blueprint('patient_auth', __name__)

@patient_auth_blueprint.route('/api/patient/register', methods=['POST'])
@capture_span()
def register_patient():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if Patient.query.filter_by(email=email).first():
            return jsonify({'message': 'Patient already exists'}), 409

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_patient = Patient(name=name, email=email, password=hashed_password)
        db.session.add(new_patient)
        db.session.commit()

        return jsonify({'message': 'Patient registered successfully', 'csrf_token': generate_csrf()}), 201
    except Exception as e:
        return jsonify({'message': 'Error during patient registration', 'error': str(e)}), 500

@patient_auth_blueprint.route('/api/patient/login', methods=['POST'])
@capture_span()
def login_patient():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        patient = Patient.query.filter_by(email=email).first()
        if patient and bcrypt.check_password_hash(patient.password, password):
            access_token = create_access_token(identity={'id': patient.id, 'role': 'patient'})
            return jsonify({'access_token': access_token, 'csrf_token': generate_csrf()}), 200

        return jsonify({'message': 'Invalid patient credentials'}), 401
    except Exception as e:
        return jsonify({'message': 'Error during patient login', 'error': str(e)}), 500
