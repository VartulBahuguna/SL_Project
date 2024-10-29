from flask import Blueprint, jsonify, send_file, current_app
from app.models import Report
from flask_jwt_extended import jwt_required, get_jwt_identity
from elasticapm import capture_span
from PyPDF2 import PdfReader, PdfWriter
import os
import io
from .. import apm

patient_blueprint = Blueprint('patient', __name__)

@patient_blueprint.route('/api/download-report/<int:report_id>', methods=['GET'])
@jwt_required()
@capture_span()
def download_report(report_id):
    try:
        user_id = get_jwt_identity()['id']
        user_role = get_jwt_identity()['role']

        report = Report.query.get(report_id)

        if not report:
            return jsonify({'message': 'Report not found'}), 404

        # Check if the user has the right to access the report
        if user_role == 'patient' and report.patient_id != user_id:
            return jsonify({'message': 'Unauthorized'}), 403
        elif user_role == 'doctor' and report.doctor_id != user_id:
            return jsonify({'message': 'Unauthorized'}), 403

        # Get the path of the PDF file
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], report.report_file)
        output_pdf = io.BytesIO()

        # Open and encrypt the PDF file
        with open(file_path, "rb") as pdf_file:
            reader = PdfReader(pdf_file)
            writer = PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            # Set password (for example, you can set it as the patient's email)
            password = f"{user_id}-secure-password"  # This should be something unique and secure
            writer.encrypt(password)

            # Write the encrypted file to a BytesIO buffer
            writer.write(output_pdf)

        output_pdf.seek(0)

        # Send the encrypted file as a response
        return send_file(
            output_pdf,
            as_attachment=True,
            download_name=f"encrypted_{report.report_file}",
            mimetype='application/pdf'
        )
    except Exception as e:
        apm.capture_exception()
        return jsonify({'message': 'Error during report download', 'error': str(e)}), 500
