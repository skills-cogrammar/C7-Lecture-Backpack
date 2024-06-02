import { Link } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Link to="/login"> Login </Link>
      <Link to="/register"> Register </Link>
      <Link to="/resource"> Resource </Link>
      <Link to="/update"> update </Link>
    </div>
  );
}

export default App;
