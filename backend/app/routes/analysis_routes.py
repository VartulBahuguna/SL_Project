from flask import Blueprint, jsonify
from app.models import User, Appointment, Report, db
from flask_jwt_extended import jwt_required
from elasticapm import capture_span
import pandas as pd
from .. import apm

analysis_blueprint = Blueprint('analysis', __name__)

@analysis_blueprint.route('/api/analysis/appointments-per-doctor', methods=['GET'])
@jwt_required()
@capture_span()
def appointments_per_doctor():
    try:
        query = db.session.query(Appointment.doctor_id, db.func.count(Appointment.id).label('appointment_count')).group_by(Appointment.doctor_id).all()
        result = [{'doctor_id': row.doctor_id, 'appointment_count': row.appointment_count} for row in query]
        return jsonify(result), 200
    except Exception as e:
        apm.capture_exception()
        return jsonify({'message': 'Error during analysis', 'error': str(e)}), 500

@analysis_blueprint.route('/api/analysis/patient-age-distribution', methods=['GET'])
@jwt_required()
@capture_span()
def patient_age_distribution():
    try:
        patients = User.query.filter_by(role='patient').all()
        patient_data = [{'id': p.id, 'date_of_birth': p.date_of_birth} for p in patients]
        patients_df = pd.DataFrame(patient_data)

        current_year = pd.Timestamp.now().year
        patients_df['birth_year'] = pd.to_datetime(patients_df['date_of_birth']).dt.year
        patients_df['age'] = current_year - patients_df['birth_year']

        bins = [0, 18, 35, 50, 100]
        labels = ['0-18', '19-35', '36-50', '51+']
        patients_df['age_group'] = pd.cut(patients_df['age'], bins=bins, labels=labels, right=False)

        age_distribution = patients_df['age_group'].value_counts().reset_index()
        age_distribution.columns = ['age_group', 'count']

        result = age_distribution.to_dict(orient='records')
        return jsonify(result), 200
    except Exception as e:
        apm.capture_exception()
        return jsonify({'message': 'Error during analysis', 'error': str(e)}), 500

@analysis_blueprint.route('/api/analysis/reports-per-doctor', methods=['GET'])
@jwt_required()
@capture_span()
def reports_per_doctor():
    try:
        query = db.session.query(Report.doctor_id, db.func.count(Report.id).label('report_count')).group_by(Report.doctor_id).all()
        result = [{'doctor_id': row.doctor_id, 'report_count': row.report_count} for row in query]
        return jsonify(result), 200
    except Exception as e:
        apm.capture_exception()
        return jsonify({'message': 'Error during analysis', 'error': str(e)}), 500
