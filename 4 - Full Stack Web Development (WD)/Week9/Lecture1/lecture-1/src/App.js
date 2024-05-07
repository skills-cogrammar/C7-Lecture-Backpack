import './App.css';
import API from "./components/api.js"
import PetCat from './components/refHook.js';

function App() {
  return (
    <div>
      <API></API>
      <PetCat></PetCat>
    </div>
  );
}

export default App;
