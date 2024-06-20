import './App.css';
import axios from 'axios';
import React, { useState, useEffect } from 'react'


function App() {
  const [defaultMessage, setDefaultMessage] = useState('This a message')
  const [customMessage, setCustomMessage] = useState('This is a custom message')

  useEffect(() => {
    const fetchData = async () => {
      try {
        const defaultResponse = await axios.get('/api/data')
        const customResponse = await axios.get('/api/custom')

        setDefaultMessage(defaultResponse.data.message);
        setCustomMessage(customResponse.data.message);
      } catch (error) {
        console.error("Error fetching data", error);
      }
    }
    
    fetchData()
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <h1>{ defaultMessage || 'Loading...' }</h1>
        <h2>{ customMessage || 'Loading...' }</h2>
      </header>
    </div>
  );
}

export default App;
