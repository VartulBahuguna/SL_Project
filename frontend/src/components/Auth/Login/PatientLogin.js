// src/components/PatientLogin.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../../../styles/login.css';

function PatientLogin() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    console.log('Patient logging in with:', { username, password });
    
    // Reset error state
    setError('');

    try {
      // Send a POST request to the backend
      const response = await fetch('http://127.0.0.1:5000/api/patient/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: username,  // assuming backend expects "email" field
          password: password,
        }),
      });

      // Check if login was successful
      if (response.ok) {
        const data = await response.json();
        console.log('Login successful:', data);

        // Save the access token (if provided) in localStorage or state
        localStorage.setItem('access_token', data.access_token);

        // Redirect to a protected route or dashboard
        navigate('/dashboard');
      } else {
        // Handle error response
        const errorData = await response.json();
        console.error('Login failed:', errorData);
        setError(errorData.message || 'Login failed. Please try again.');
      }
    } catch (err) {
      console.error('Error during login:', err);
      setError('An error occurred. Please try again later.');
    }

    // Clear input fields after submission
    setUsername('');
    setPassword('');
  };

  return (
    <div className="login-page">
      <div className="login-container">
        <button className="home-button" onClick={() => navigate('/')}><span>&larr; </span></button>
        <form className="login-form" onSubmit={handleLogin}>
          <h2>Patient Login</h2>
          {error && <p className="error-message">{error}</p>}
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <button type="submit">Login</button>
          <p className="signup-note">
            Don’t have an account? <a href="/patient-signup">Sign up here</a>.
          </p>
        </form>
      </div>
    </div>
  );
}

export default PatientLogin;
