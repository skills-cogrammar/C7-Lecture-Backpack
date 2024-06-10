import { useContext } from "react";
import GrandParent from "./components/GrandParent";
import { ThemeContext } from "./context/themeContext";

function App() {
  const { theme, handleTheme, changeColor } = useContext(ThemeContext);
  return (
    <div style={changeColor}>
      <button onClick={handleTheme}>Change Theme</button>
      <h1> {theme} </h1>
      <GrandParent />
    </div>
  );
}

export default App;
