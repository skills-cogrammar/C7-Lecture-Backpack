import { useState } from "react"
import axios from "axios"

function App() {

  const fetchHome = async ()=>{
    const response = await axios.get("http://localhost:8000/")
    console.log(response)
  }

  
  fetchHome()


  return (
    <div className="App">
    </div>
  );
}

export default App;
