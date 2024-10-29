from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
from app.models import Report, db
from flask_jwt_extended import jwt_required, get_jwt_identity
from elasticapm import capture_span
import os
from .. import apm

doctor_blueprint = Blueprint('doctor', __name__)

@doctor_blueprint.route('/api/upload-report', methods=['POST'])
@jwt_required()
@capture_span()
def upload_report():
    try:
        user_id = get_jwt_identity()['id']
        user_role = get_jwt_identity()['role']

        if user_role != 'doctor':
            return jsonify({'message': 'Unauthorized'}), 403

        if 'file' not in request.files:
            return jsonify({'message': 'No file part'}), 400

        file = request.files['file']
        patient_id = request.form.get('patient_id')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            new_report = Report(patient_id=patient_id, doctor_id=user_id, report_file=filename)
            db.session.add(new_report)
            db.session.commit()

            return jsonify({'message': 'Report uploaded successfully'}), 201
        else:
            return jsonify({'message': 'Invalid file format. Only PDFs allowed.'}), 400
    except Exception as e:
        apm.capture_exception()
        return jsonify({'message': 'Error during report upload', 'error': str(e)}), 500

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'pdf'
