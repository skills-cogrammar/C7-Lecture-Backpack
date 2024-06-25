import { useContext, useEffect } from "react";
import { ThemeContext } from "./context/ThemeContext";
import NavBar from "./components/NavBar";
import { AuthContext } from "./context/AuthContext";

function App() {
  const { theme, handleTheme, currentBackground } = useContext(ThemeContext);
  const { token } = useContext(AuthContext);

  return (
    <div style={currentBackground}>
      <NavBar />
      {token ? (
        <button onClick={handleTheme}>Switch {theme}</button>
      ) : (
        <h1>Please log in</h1>
      )}
    </div>
  );
}

export default App;
