import axios from 'axios';
import React, { useState, useEffect } from 'react'


const Messages = () => {
    const [defaultMessage, setDefaultMessage] = useState('This a message');
    const [customMessage, setCustomMessage] = useState('This is a custom message');

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
        <div>
            <header className="App-header">
                <h1>{ defaultMessage }</h1>
                <h2>{ customMessage }</h2>
            </header>
        </div>
    )
}

export default Messages;