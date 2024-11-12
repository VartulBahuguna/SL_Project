// src/components/DoctorLogin.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../../../styles/login.css';

function DoctorLogin() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    console.log('Doctor logging in with:', { username, password });
    setUsername('');
    setPassword('');
  };

  return (
    <div className="login-page">
      <div className="login-container">
        <button className="home-button" onClick={() => navigate('/')}><span>&larr; </span></button>
        <form className="login-form" onSubmit={handleLogin}>
          <h2>Doctor Login</h2>
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
            Don’t have an account? <a href="/doctor-signup">Sign up here</a>.
          </p>
        </form>
      </div>
    </div>
  );
}

export default DoctorLogin;
