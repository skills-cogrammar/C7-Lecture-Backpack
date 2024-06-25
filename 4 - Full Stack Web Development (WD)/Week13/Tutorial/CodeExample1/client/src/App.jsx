import { useEffect } from "react"

function App() {

  const fetchTest = async ()=>{
    const response = await fetch("http://localhost:8000/")
    const data = await response.json()
    console.log(data)
  }

  useEffect(()=>{
    fetchTest()
  }, [])

  return (
    <>
    </>
  )
}

export default App
