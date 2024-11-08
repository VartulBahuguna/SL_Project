import React from 'react';
import '../../styles/Profile.css';

function DoctorProfile() {
  return (
    <div className="profile-container">
      <h2>Doctor Profile</h2>
      <div className="profile-info">
        <label>Name:</label>
        <p>Dr. Sachin H.N</p>

        <label>Specialization:</label>
        <p>Cardiac Anesthetist</p>

        <label>Contact:</label>
        <p>dr.sachin@example.com</p>

        <label>Availability:</label>
        <p>Monday - Friday, 9:00 AM - 5:00 PM</p>
        
        <button className="edit-button">Edit Profile</button>
      </div>
    </div>
  );
}

export default DoctorProfile;
