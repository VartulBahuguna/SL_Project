import React, { useState } from 'react';
import './Appointments.css';

function ScheduleAppointment() {
  const [appointmentDate, setAppointmentDate] = useState('');
  const [doctorName, setDoctorName] = useState('');

  const handleAppointmentRequest = (e) => {
    e.preventDefault();
    console.log('Appointment requested for', doctorName, 'on', appointmentDate);
    // Add API call or additional functionality here
  };

  return (
    <div className="appointment-container">
      <h2>Schedule an Appointment</h2>
      <form onSubmit={handleAppointmentRequest} className="appointment-form">
        <label>Doctor:</label>
        <input
          type="text"
          placeholder="Enter doctor's name"
          value={doctorName}
          onChange={(e) => setDoctorName(e.target.value)}
        />
        
        <label>Appointment Date:</label>
        <input
          type="date"
          value={appointmentDate}
          onChange={(e) => setAppointmentDate(e.target.value)}
        />

        <button type="submit">Request Appointment</button>
      </form>
    </div>
  );
}

export default ScheduleAppointment;
