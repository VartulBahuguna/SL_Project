import React from 'react';
import '../../styles/Profile.css';

function PatientProfile() {
  return (
    <div className="profile-container">
      <h2>Patient Profile</h2>
      <div className="profile-info">
        <label>Name:</label>
        <p>John Doe</p>

        <label>Contact:</label>
        <p>john.doe@example.com</p>

        <label>Medical ID:</label>
        <p>123456789</p>
        
        <button className="edit-button">Edit Profile</button>
      </div>
    </div>
  );
}

export default PatientProfile;
