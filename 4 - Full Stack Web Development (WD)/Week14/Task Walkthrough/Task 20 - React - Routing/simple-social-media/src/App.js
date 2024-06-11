import './App.css';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from './components/Home';
import Profiles from './components/Profiles';
import About from './components/About';
import Profile from './components/Profile';

function App() {
  return (
    <Router>
      <div className='App'>
        <nav>
          <Link to="/">Home</Link>
          <Link to="/profiles">Profiles</Link>
          <Link to="/about">About</Link>
        </nav>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/profiles' element={<Profiles />} />
          <Route path='/profile/:id' element={<Profile />} />
          <Route path='/about' element={<About />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
