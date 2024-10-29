import React from 'react';
import { downloadReport } from '../api';

function Dashboard() {
  const token = localStorage.getItem('token');

  const handleDownloadReport = async (reportId) => {
    try {
      const response = await downloadReport(reportId, token);
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `report_${reportId}.pdf`);
      document.body.appendChild(link);
      link.click();
    } catch (error) {
      alert('Error downloading report');
    }
  };

  return (
    <div>
      <h1>Dashboard</h1>
      <button onClick={() => handleDownloadReport(1)}>Download Report 1</button>
      <button onClick={() => handleDownloadReport(2)}>Download Report 2</button>
    </div>
  );
}

export default Dashboard;
