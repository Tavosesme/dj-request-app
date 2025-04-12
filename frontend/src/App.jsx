
import React, { useState } from 'react';

function App() {
  const [song, setSong] = useState('');
  const [dedication, setDedication] = useState('');
  const [dj, setDJ] = useState('');

  const handleSubmit = async () => {
    const res = await fetch('https://dj-request-app.onrender.com/create-request', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ song, dedication, dj })
    });
    const data = await res.json();
    alert('Solicitud enviada con ID: ' + data.request_id);
  };

  return (
    <div>
      <h1>Pedir canción</h1>
      <input placeholder='Nombre DJ' onChange={(e) => setDJ(e.target.value)} /><br/>
      <input placeholder='Canción' onChange={(e) => setSong(e.target.value)} /><br/>
      <input placeholder='Dedicatoria' onChange={(e) => setDedication(e.target.value)} /><br/>
      <button onClick={handleSubmit}>Enviar</button>
    </div>
  );
}

export default App;
