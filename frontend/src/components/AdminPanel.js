import React, { useState } from 'react';
import { assignDoctor } from '../api';

function AdminPanel() {
  const [appointmentId, setAppointmentId] = useState('');
  const [doctorId, setDoctorId] = useState('');
  const token = localStorage.getItem('token');

  const handleAssignDoctor = async (e) => {
    e.preventDefault();
    try {
      await assignDoctor(appointmentId, doctorId, token);
      alert('Doctor assigned successfully');
    } catch (error) {
      alert('Error assigning doctor');
    }
  };

  return (
    <form onSubmit={handleAssignDoctor}>
      <input type="text" placeholder="Appointment ID" value={appointmentId} onChange={(e) => setAppointmentId(e.target.value)} required />
      <input type="text" placeholder="Doctor ID" value={doctorId} onChange={(e) => setDoctorId(e.target.value)} required />
      <button type="submit">Assign Doctor</button>
    </form>
  );
}

export default AdminPanel;
