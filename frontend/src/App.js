import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './components/Auth/Login';
import PatientDashboard from './components/Dashboard/PatientDashboard';
import DoctorDashboard from './components/Dashboard/DoctorDashboard';
import AdminDashboard from './components/Dashboard/AdminDashboard';
import PatientProfile from './components/Profile/PatientProfile';
import DoctorProfile from './components/Profile/DoctorProfile';
import ScheduleAppointment from './components/Appointments/ScheduleAppointment';
import Reports from './components/Reports/Reports';
import ReportSummarization from './components/Reports/ReportSummarization';
import Statistics from './components/Analytics/Statistics';
import NotFound from './components/NotFound';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/patient-dashboard" element={<PatientDashboard />} />
        <Route path="/doctor-dashboard" element={<DoctorDashboard />} />
        <Route path="/admin-dashboard" element={<AdminDashboard />} />
        <Route path="/patient-profile" element={<PatientProfile />} />
        <Route path="/doctor-profile" element={<DoctorProfile />} />
        <Route path="/schedule-appointment" element={<ScheduleAppointment />} />
        <Route path="/reports" element={<Reports />} />
        <Route path="/summarize-report" element={<ReportSummarization />} />
        <Route path="/admin-dashboard/statistics" element={<Statistics />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Router>
  );
}

export default App;
