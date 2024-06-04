import './App.css';
import Welcome from "./components/welcome.js";
import Message from "./components/message.js";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Welcome number = "14"></Welcome>
        <Message topic = "React.js"></Message>
      </header>
    </div>
  );
}

export default App;
