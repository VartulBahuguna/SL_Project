import React from 'react';
import { useNavigate } from 'react-router-dom'; // Assumes React Router is used for navigation
import '../../styles/Dashboard.css';

function DoctorDashboard() {
  const navigate = useNavigate();

  return (
    <div className="dashboard">
      <h2 className="dashboard-title">Doctor Dashboard</h2>
      <div className="dashboard-buttons">
        <button 
          className="dashboard-button" 
          onClick={() => navigate('/view-patients')} // URL for View Patients section
        >
          View Patients
        </button>
        <button 
          className="dashboard-button" 
          onClick={() => navigate('/upload-reports')} // URL for Upload Reports section
        >
          Upload Reports
        </button>
        <button 
          className="dashboard-button" 
          onClick={() => navigate('/manage-schedule')} // URL for Manage Schedule section
        >
          Manage Schedule
        </button>
        <button 
          className="dashboard-button" 
          onClick={() => navigate('/about-me')} // URL for About Me/Profile Settings section
        >
          About Me
        </button>
      </div>
    </div>
  );
}

export default DoctorDashboard;
