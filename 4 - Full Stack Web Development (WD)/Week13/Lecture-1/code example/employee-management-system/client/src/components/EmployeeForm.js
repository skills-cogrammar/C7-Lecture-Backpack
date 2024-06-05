import React, { useState } from 'react';
import axios from 'axios';

function EmployeeForm({ employee, setEmployees, setIsEditing, setEditingEmployee }) {
    const [formData, setFormData] = useState({
        name: employee ? employee.name : '',
        position: employee ? employee.position : '',
        office: employee ? employee.office : '',
        salary: employee ? employee.salary : ''
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (employee) {
            // Update existing employee
            const updatedEmployee = await axios.patch(`http://localhost:5000/employees/${employee._id}`, formData);
            setEmployees(prev => prev.map(item => item._id === employee._id ? updatedEmployee.data : item));
        } else {
            // Add new employee
            const newEmployee = await axios.post('http://localhost:5000/employees', formData);
            setEmployees(prev => [...prev, newEmployee.data]);
        }
        // Reset Form
        setFormData({
            name: '',
            position: '',
            office: '',
            salary: ''
        });
        if (setIsEditing) setIsEditing(false);
        if (setEditingEmployee) setEditingEmployee(null);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" name="name" value={formData.name} onChange={handleChange} placeholder="Name" required />
            <input type="text" name="position" value={formData.position} onChange={handleChange} placeholder="Position" required />
            <input type="text" name="office" value={formData.office} onChange={handleChange} placeholder="Office" required />
            <input type="number" name="salary" value={formData.salary} onChange={handleChange} placeholder="Salary" required />
            <button type="submit">{employee ? 'Update' : 'Add'}</button>
            {employee && <button onClick={() => setIsEditing(false)}>Cancel</button>}
        </form>
    );
}

export default EmployeeForm;
