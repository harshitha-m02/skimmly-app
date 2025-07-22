import React, { useState } from 'react';

export default function UploadDocument() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      setMessage('');
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setMessage('Please select a file to upload.');
      return;
    }

    // Example: simulate upload
    const formData = new FormData();
    formData.append('document', file);

    try {
      // Replace with your actual backend URL
      // const res = await fetch("http://localhost:8000/upload", {
      //   method: 'POST',
      //   body: formData,
      // });

      // const result = await res.json();
      // setMessage(`Upload successful: ${result.filename}`);

      // Simulate successful upload
      setTimeout(() => {
        setMessage(`Upload successful: ${file.name}`);
      }, 1000);
    } catch (error) {
      console.error(error);
      setMessage('Upload failed. Please try again.');
    }
  };

  return (
    <div className="max-w-md mx-auto mt-10 p-6 border rounded-xl shadow-lg bg-white">
      <h2 className="text-2xl font-semibold mb-4">Upload a Document</h2>
      <input
        type="file"
        accept=".pdf,.doc,.docx,.txt"
        onChange={handleFileChange}
        className="mb-4 block w-full text-sm text-gray-700"
      />
      <button
        onClick={handleUpload}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
      >
        Upload
      </button>
      {file && <p className="mt-2 text-sm text-gray-600">Selected: {file.name}</p>}
      {message && <p className="mt-4 text-sm text-green-600">{message}</p>}
    </div>
  );
}
