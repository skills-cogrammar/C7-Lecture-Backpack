import { useState, useEffect } from "react";
const Employee = () => {
  const [employees, setEmployees] = useState([]);
  const [ name, setName ] = useState("")
  const [ role, setRole] = useState("")

  const fetchEmployees = async () => {
    const response = await fetch("http://localhost:8000/employees");
    const data = await response.json();
    setEmployees(data.employees);
  };

  useEffect(() => {
    fetchEmployees();
  }, [employees]);

  const updateEmployee = async (id)=>{
    const response = await fetch(`http://localhost:8000/employees/update/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type" :"application/json"
        },
        body: JSON.stringify({
            name,
            role
        })
    })
    const data = await response.json()
    console.log(data)
  }

  return (
    <>
      <h1>Employees</h1>
      {employees.map((employee, index) => {
        return (
          <div key={index} className="flex gap-2 flex-col">
            <p>
              Name: <span className="text-orange-500">{employee.name}</span>
            </p>
            <p>
              Role: <span className="text-orange-500">{employee.role}</span>
            </p>

            <form onSubmit={(e)=>e.preventDefault()}>
              <input
                value={name}
                className="block w-full rounded-md border-0 py-1.5 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                placeholder="Update name"
                onChange={(e)=>setName(e.target.value)}
              />
              <input
                value={role}
                className="block w-full rounded-md border-0 py-1.5 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                placeholder="Update name"
                onChange={(e)=>setRole(e.target.value)}
              />
              <button className="bg-orange-500 p-2 text-white rounded-md" onClick={(e)=>updateEmployee(employee._id)}>Update Employee</button>
            </form>
          </div>
        );
      })}
    </>
  );
};

export default Employee;
