import React from 'react';
import { useNavigate } from 'react-router-dom'; // Assumes React Router is used for navigation
import '../../styles/Dashboard.css';

function AdminDashboard() {
  const navigate = useNavigate();

  return (
    <div className="dashboard">
      <h2 className="dashboard-title">Admin Dashboard</h2>
      <div className="dashboard-buttons">
        <button 
          className="dashboard-button" 
          onClick={() => navigate('/manage-doctors')} // URL for Manage Doctors section
        >
          Manage Doctors
        </button>
        <button 
          className="dashboard-button" 
          onClick={() => navigate('/patient-assignment')} // URL for Patient Assignment section
        >
          Patient Assignment
        </button>
        <button 
          className="dashboard-button" 
          onClick={() => navigate('/view-statistics')} // URL for View Statistics section
        >
          View Statistics
        </button>
      </div>
    </div>
  );
}

export default AdminDashboard;
