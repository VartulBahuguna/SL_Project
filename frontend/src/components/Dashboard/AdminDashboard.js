import React from 'react';
import './Dashboard.css';

function AdminDashboard() {
  return (
    <div className="dashboard">
      <h2>Admin Dashboard</h2>
      <div className="dashboard-cards">
        <div className="card">
          <h3>Manage Doctors</h3>
          <p>Add, view, and assign doctors to patients.</p>
        </div>
        <div className="card">
          <h3>Patient Assignment</h3>
          <p>Assign patients to doctors based on appointment requests.</p>
        </div>
        <div className="card">
          <h3>View Statistics</h3>
          <p>Access platform statistics like doctor-patient ratio.</p>
        </div>
      </div>
    </div>
  );
}

export default AdminDashboard;
