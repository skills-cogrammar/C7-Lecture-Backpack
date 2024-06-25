import './App.css';
import EmployeeForm from './components/EmployeeForm';
import EmployeeList from './components/EmployeeList';

function App() {
  return (
    <div className="App">
      <h2>Employee Management System</h2>

      <EmployeeForm />
      <EmployeeList />
    </div>
  );
}

export default App;
