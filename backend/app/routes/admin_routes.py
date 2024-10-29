from flask import Blueprint, request, jsonify
from app.models import User, db, Appointment
from flask_jwt_extended import jwt_required, get_jwt_identity
from elasticapm import capture_span
from tasks import assign_doctors
from .. import apm

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/api/admin/assign-doctors', methods=['POST'])
@jwt_required()
@capture_span()
def manual_assign_doctors():
    try:
        # Check if the user is an admin
        user_id = get_jwt_identity()['id']
        user = User.query.get(user_id)
        if not user or user.role != 'admin':
            return jsonify({'message': 'Unauthorized'}), 403

        # Trigger the doctor assignment task
        assign_doctors.apply_async()
        return jsonify({'message': 'Doctor assignment task triggered'}), 202
    except Exception as e:
        apm.capture_exception()
        return jsonify({'message': 'Error triggering doctor assignment', 'error': str(e)}), 500

@admin_blueprint.route('/api/admin/add-doctor', methods=['POST'])
@jwt_required()
@capture_span()
def add_doctor():
    try:
        # Check if the user is an admin
        user_id = get_jwt_identity()['id']
        user = User.query.get(user_id)
        if not user or user.role != 'admin':
            return jsonify({'message': 'Unauthorized'}), 403

        data = request.json
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not (name and email and password):
            return jsonify({'message': 'Invalid data'}), 400

        # Check if the doctor already exists
        if User.query.filter_by(email=email).first():
            return jsonify({'message': 'Doctor already exists'}), 409

        # Create a new doctor user
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_doctor = User(name=name, email=email, password=hashed_password, role='doctor')
        db.session.add(new_doctor)
        db.session.commit()

        return jsonify({'message': 'Doctor added successfully', 'doctor_id': new_doctor.id}), 201
    except Exception as e:
        apm.capture_exception()
        return jsonify({'message': 'Error adding doctor', 'error': str(e)}), 500

@admin_blueprint.route('/api/admin/assign-patient/<int:appointment_id>', methods=['POST'])
@jwt_required()
@capture_span()
def assign_patient(appointment_id):
    try:
        # Check if the user is an admin
        user_id = get_jwt_identity()['id']
        user = User.query.get(user_id)
        if not user or user.role != 'admin':
            return jsonify({'message': 'Unauthorized'}), 403

        data = request.json
        doctor_id = data.get('doctor_id')

        # Fetch the appointment
        appointment = Appointment.query.get(appointment_id)
        if not appointment:
            return jsonify({'message': 'Appointment not found'}), 404

        # Assign the doctor to the appointment
        appointment.doctor_id = doctor_id
        db.session.commit()

        return jsonify({'message': 'Patient assigned to doctor successfully'}), 200
    except Exception as e:
        apm.capture_exception()
        return jsonify({'message': 'Error assigning patient to doctor', 'error': str(e)}), 500
