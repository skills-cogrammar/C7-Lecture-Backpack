### Task: Employee Record Management System

#### Objective:
Develop a simple script using Node.js and Lodash to manage a list of employee records. The script will perform various operations on the employee data, including sorting, filtering, and updating records.

#### Initial Setup:
1. Create a new directory for your project and navigate into it.
2. Initialize a Node.js project:
   ```bash
   npm init -y
   ```
3. Install Lodash:
   ```bash
   npm install lodash
   ```

#### Task Description:
You will create a script that manages an array of employee objects. Each employee object will have the following structure:
```javascript
{
    id: Number,
    name: String,
    department: String,
    salary: Number
}
```

#### Detailed Steps:
1. **Create Sample Data**:
   - Define an array named `employees` that contains at least 10 employee objects with varying attributes.

2. **Implement Functionality Using Lodash**:
   - **Filter Employees by Department**:
     Write a function that uses `_.filter` to return all employees in a specified department.
   - **Sort Employees by Salary**:
     Write a function that uses `_.sortBy` to return the employees sorted by salary in ascending order.
   - **Increase Salary**:
     Write a function that uses `_.map` to increase the salary of all employees by a specified percentage.
   - **Find an Employee by ID**:
     Write a function that uses `_.find` to find and return an employee by their ID.
   - **Remove an Employee**:
     Write a function that uses `_.remove` to delete an employee from the array based on ID.

3. **Testing Your Functions**:
   - Test each function separately to ensure it performs the intended operation. You can use console.log to print the results of each operation to the console.

#### Extension Ideas:
- Add a function to calculate the average salary in a department.
- Implement a way to serialize the modified employees array to a JSON file after operations.