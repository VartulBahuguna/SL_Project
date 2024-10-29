from flask import Blueprint, request, jsonify
from app.models import User, db
from .. import bcrypt, jwt
from flask_jwt_extended import create_access_token
from elasticapm import capture_span
from flask_wtf.csrf import generate_csrf
from .. import apm

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/api/register', methods=['POST'])
@capture_span()
def register():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        role = data.get('role', 'patient')

        if User.query.filter_by(email=email).first():
            return jsonify({'message': 'User already exists'}), 409

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(name=name, email=email, password=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully', 'csrf_token': generate_csrf()}), 201
    except Exception as e:
        apm.capture_exception()
        return jsonify({'message': 'Error during registration', 'error': str(e)}), 500

@auth_blueprint.route('/api/login', methods=['POST'])
@capture_span()
def login():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            access_token = create_access_token(identity={'id': user.id, 'role': user.role})
            return jsonify({'access_token': access_token, 'csrf_token': generate_csrf()}), 200

        return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        apm.capture_exception()
        return jsonify({'message': 'Error during login', 'error': str(e)}), 500
