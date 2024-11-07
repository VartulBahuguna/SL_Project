import React from 'react';
import './Dashboard.css';

function PatientDashboard() {
  return (
    <div className="dashboard">
      <h2>Patient Dashboard</h2>
      <div className="dashboard-cards">
        <div className="card">
          <h3>View Reports</h3>
          <p>Access your medical reports and scan images here.</p>
        </div>
        <div className="card">
          <h3>Request Appointment</h3>
          <p>Schedule a meeting with your healthcare provider.</p>
        </div>
        <div className="card">
          <h3>Medical History</h3>
          <p>Review your medical history and past appointments.</p>
        </div>
      </div>
    </div>
  );
}

export default PatientDashboard;
