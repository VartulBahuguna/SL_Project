// src/components/Login.js
import React, { useState } from 'react';
import '../../styles/login.css';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = (e) => {
    e.preventDefault();
    console.log('Logging in with:', { username, password });
  };

  return (
    <div className="login-page">
      <div className="login-container">
        <form className="login-form" onSubmit={handleLogin}>
          <h2>Login to Medical Platform</h2>
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
            Don't have an account? <a href="/signup">Sign up here</a>.
          </p>
        </form>
      </div>
    </div>
  );
}

export default Login;
