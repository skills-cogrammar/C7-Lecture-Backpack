import './App.css';
import Counter from "./components/counter.js"
import userContext from "./components/userContext.js"

function App() {
  return (
    <userContext.Provider value="Zahra"> 
      <Counter></Counter>
    </userContext.Provider>
  );
}

export default App;
