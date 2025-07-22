import React, { useState, useEffect } from 'react';
import UploadDocument from './UploadDocument';

import axios from 'axios';

function App() {
  // const [data, setData] = useState('');

  // useEffect(() => {
  //   axios.get('http://localhost:8000/api/data') // Adjust port if using FastAPI (e.g., 8000)
  //     .then(response => {
  //       setData(response.data.message);
  //     })
  //     .catch(error => {
  //       console.error('Error fetching data:', error);
  //     });
  // }, []);

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <h1>uploadDocument</h1>
      <UploadDocument/>
    </div>
  );
}

export default App;