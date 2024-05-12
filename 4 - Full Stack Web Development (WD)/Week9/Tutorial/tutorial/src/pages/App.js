import { Link } from "react-router-dom";

function App() {
  return (
  <div className="App">
    <h1>Home Page</h1>
    <Link to='/users'>Users' Page</Link>
  </div>
  );
}

export default App;