import './App.css';
import StyledButton from "./components/styledButtonComp.js"

function App() {
  function handleClick (event) {
    alert("Button 1 clicked!");
    event.preventDefault();
    event.stopPropagation();
  }

  function handleClick_2() {
    alert("Button 2 clicked!");
  }

  function submit (event) {
    alert(`Thank you for submitting your form`);
  }

  return (
    <div>
      <form onSubmit = {submit} onClick = {handleClick}>
        <StyledButton type = 'submit' func = {handleClick}></StyledButton>
      </form>

      <StyledButton func = {handleClick_2}></StyledButton>
    </div>
  );
}

export default App;
