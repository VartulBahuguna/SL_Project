// src/components/PatientSignUp.js
import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../../../styles/signup.css';

function PatientSignUp() {
  const navigate = useNavigate();

  return (
    <div className="signup-page">
      <div className="signup-container">
        <button className="home-button" onClick={() => navigate('/')}><span>&larr; </span></button>
        <h2>Patient Sign Up</h2>
        <p>Create your account to manage your medical records and appointments.</p>
        <form className="signup-form">
          <input type="text" placeholder="Full Name" required />
          <input type="email" placeholder="Email" required />
          <input type="password" placeholder="Password" required />
          <input type="password" placeholder="Confirm Password" required />
          <button type="submit">Sign Up</button>
        </form>
        <p className="signup-note">Already have an account? <a href="/patient-login">Login here</a>.</p>
      </div>
    </div>
  );
}

export default PatientSignUp;
