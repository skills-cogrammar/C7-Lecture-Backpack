import './App.css';
import API from "./components/api.js"
import PetCat from './components/refHook.js';
import AutoFocusInput from './components/autofocus.js';

function App() {
  return (
    <div>
      <API></API>
      <PetCat></PetCat>
      <AutoFocusInput></AutoFocusInput>
    </div>
  );
}

export default App;
