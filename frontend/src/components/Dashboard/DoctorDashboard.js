import React from 'react';
import '../../styles/Dashboard.css';

function DoctorDashboard() {
  return (
    <div className="dashboard">
      <h2>Doctor Dashboard</h2>
      <div className="dashboard-cards">
        <div className="card">
          <h3>View Patients</h3>
          <p>Access a list of your assigned patients and their medical history.</p>
        </div>
        <div className="card">
          <h3>Upload Reports</h3>
          <p>Upload new reports, scan images, and notes for your patients.</p>
        </div>
        <div className="card">
          <h3>Manage Schedule</h3>
          <p>View and update your appointment schedule.</p>
        </div>
      </div>
    </div>
  );
}

export default DoctorDashboard;
