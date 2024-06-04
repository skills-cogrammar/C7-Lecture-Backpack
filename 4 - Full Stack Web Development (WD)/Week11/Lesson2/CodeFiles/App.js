// Remember to import React and Axios 
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
    // Create a state variable using the useState hook
    // This will store the fetched data
    const [data, setData] = useState({}); 

    // Use the useEffect hook to run the fetch data function
    // This is necessary because this is an async function
    useEffect(() => {
        fetchData();
    }, []);


    // Asychronous function which fetches data from the backend via axios
    // This happens in the background and stores the data in the state variable
    const fetchData = async () => {
        try {
        const response = await axios.get('/api/data');
        setData(response.data);
        } catch (error) {
        console.error('Error fetching data:', error);
        }
    };

    // This displays the fetched data to the user on the React app
    return (
        <div className="App">
        <header className="App-header">
            <h1>{data.message || 'Loading...'}</h1>
        </header>
        </div>
    );
}
export default App;

