import React, { useEffect, useState } from 'react';
import axios from 'axios';
import EmployeeForm from './EmployeeForm';

function EmployeeList() {
    const [employees, setEmployees] = useState([]);
    const [isEditing, setIsEditing] = useState(false);
    const [editingEmployee, setEditingEmployee] = useState(null);

    useEffect(() => {
        async function fetchEmployees() {
            const result = await axios.get('http://localhost:5000/employees');
            setEmployees(result.data);
        }
        fetchEmployees();
    }, []);

    const handleDelete = async (id) => {
        await axios.delete(`http://localhost:5000/employees/${id}`);
        setEmployees(prev => prev.filter(employee => employee._id !== id));
    };

    return (
        <div>
            {isEditing ? (
                <EmployeeForm employee={editingEmployee} setEmployees={setEmployees} setIsEditing={setIsEditing} setEditingEmployee={setEditingEmployee} />
            ) : (
                <>
                    <button onClick={() => { setIsEditing(true); setEditingEmployee(null); }}>Add Employee</button>
                    <table>
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Position</th>
                                <th>Office</th>
                                <th>Salary</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            {employees.map((employee) => (
                                <tr key={employee._id}>
                                    <td>{employee.name}</td>
                                    <td>{employee.position}</td>
                                    <td>{employee.office}</td>
                                    <td>{employee.salary}</td>
                                    <td>
                                        <button onClick={() => { setIsEditing(true); setEditingEmployee(employee); }}>Edit</button>
                                        <button onClick={() => handleDelete(employee._id)}>Delete</button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </>
            )}
        </div>
    );
}

export default EmployeeList;
