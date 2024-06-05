// import the lodash module
const lodash = require('lodash')

// sample employee data
let employees = [
    { id: 1, name: "Alice", department: "Engineering", salary: 50000 },
    { id: 2, name: "Bob", department: "HR", salary: 40000 },
    { id: 3, name: "Charlie", department: "Engineering", salary: 60000 },
    { id: 4, name: "David", department: "Marketing", salary: 45000 },
    { id: 5, name: "Eve", department: "HR", salary: 48000 },
    { id: 6, name: "Frank", department: "Marketing", salary: 52000 },
    { id: 7, name: "Grace", department: "Engineering", salary: 75000 },
    { id: 8, name: "Hannah", department: "HR", salary: 35000 },
    { id: 9, name: "Ian", department: "Engineering", salary: 65000 },
    { id: 10, name: "Judy", department: "Marketing", salary: 47000 }
]

// Function that filters the employees by departments using the lodash filter function
function empDepartment(department) {
    const mydepartment = lodash.filter(employees, { department: department });
    return mydepartment;
}

// sorts the employees by salary using the lodash sortBy function
function empSalary() {
    const mysalary = lodash.sortBy(employees, 'salary');
    return mysalary;
}

// increases the employee salary based on percentage using the lodash map function
function increaseSalary(percentage) {
    const newSalary = lodash.map(employees, employee => {
        employee.salary += employee.salary * percentage / 100;
        
        return employee;
    })

    return newSalary;
}

console.log(empDepartment('Engineering'));
// console.log(empSalary());

// console.log(increaseSalary(100));