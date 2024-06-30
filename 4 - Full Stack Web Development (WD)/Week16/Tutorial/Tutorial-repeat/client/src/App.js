import { gql, useMutation, useQuery } from "@apollo/client";
import Update from "./components/Update";

const READ_EMPLOYEES = gql`
  query ReadEmployees {
    employees {
      email
      lineManager
      name
      role
      id
    }
  }
`;

const DELETE_EMPLOYEE = gql`
mutation DeleteEmployee($deleteEmployeeId: ID) {
  deleteEmployee(id: $deleteEmployeeId) {
    email
    id
    lineManager
    name
    role
  }
}
`;

function App() {
  const { data, loading, error } = useQuery(READ_EMPLOYEES)
  const [deleteEmployee, { data:deletedEmployee, error: deleteError, loading: loadingDelete }] = useMutation(DELETE_EMPLOYEE)

  if (loading) return <h1>Loading...</h1>;
  if (error) return <h1>Error in fetching data</h1>;
  if (loadingDelete) return <h1>Deleting</h1>
  if (deleteError) return <h1>Error in deleting</h1>

  console.log(deletedEmployee);
  console.log(data)

  const handleDelete = (id)=>{
    deleteEmployee({ variables: {deleteEmployeeId: id}})

  }

  return (
    <>
      {data.employees.map((employee) => {
        return (
          <div key={employee.id}>
            <p> Name: {employee.name}</p>
            <p> Role: {employee.role}</p>
            <p> LineManager: {employee.lineManager} </p>

            <button onClick={()=> handleDelete(employee.id)}>DELETE</button>
          </div>
        );
      })}

      <Update />
    </>
  );
}

export default App;
