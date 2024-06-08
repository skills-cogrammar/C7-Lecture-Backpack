import { useState } from "react"
import Increment from "./components/Increment"
import Decrement from "./components/Decrement"
import Display from "./components/Display"
function App() {
  /**
   * item1 -> state variable
   * item2 -> function to manipulate the state
   * useState(argument) -> argument === initial value of item1(count variable)
   */
  const [ count, setCount ] = useState(10)

  const increment = (num)=>{
    //perform an increment
    setCount(count + parseFloat(num))
  }

  const decrement = (num)=>{
    //perform a decrement
    if (count - parseFloat(num) >= 0) {
      setCount(count - parseFloat(num))
    } else {
      alert("You have a negative count value")
    }
  }

  return (
    <>
    <Display count={count}/>
    <Increment increment={increment}/>
    <Decrement decrement={decrement}/>
    </>
  )
}

export default App
