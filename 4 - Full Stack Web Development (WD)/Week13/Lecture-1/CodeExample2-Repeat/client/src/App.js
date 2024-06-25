import { useState, useEffect } from "react"
import Employee from "./components/Employee"
import CreateEmployee from "./components/CreateEmployee"

function App() {

  const [ message, setMessage ] = useState("")


  const fetchMessage = async ()=>{
    const response = await fetch("http://localhost:8000") //GET is the default method
    const data = await response.json()
    setMessage(data.message)

  }

  useEffect(()=>{
    fetchMessage()
  }, [])//Only fetch the API once when the component renders


  return (
    <div>
      { message }
      <Employee/>
      <CreateEmployee/>
    </div>
  );
}

export default App;
