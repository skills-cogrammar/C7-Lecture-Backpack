import './App.css';
import Welcome from "./Welcome";

let name = "Zahra Mohamed";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1> Welcome everyone! I'm {name}</h1>
        <Welcome number = "68" />
      </header>
    </div>
  );
}

export default App;
