import './App.css';
import axios from 'axios';
import {useState, useEffect} from 'react';

function App() {
  // State variable
  const [data, setData] = useState({});

  // useEffect
  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get('/api/data');
      setData(response.data);
    } catch (error) {
      console.error("Error while fetching data from backend", error);
    }
  }

  return (
    <div className = "App"> 
      <header className = "App-header">
        <h1> {data.message || "Loading..."} </h1>
      </header>
    </div>
  )
}

export default App;
