const {Employee} = require("../models/Employee")


const getHelloWorld = (req, res)=>{
    res.json({
        message: "Hello World"
    })
}


const getEmployees = async (req, res)=>{
    const employees = await Employee.find()
    res.json({
        message: `Employees found ${employees.length}`,
        employees: employees
    })
}

const createEmployees = async (req, res)=>{
    const { name, role } = req.body

    const newUser = await Employee.create({
        name: name,
        role: role
    })

    res.status(201).json({
        message: "User created successfully",
        newUser: newUser
    })
}

const updateEmployee = async (req, res)=>{
    const { id } = req.params
    const { name, role } = req.body

    const updatedEmployee = await Employee.findByIdAndUpdate(id, {name, role})
    res.json({
        message: "Employee Updated",
        employee: updateEmployee
    })
}


module.exports = {
    getHelloWorld,
    getEmployees,
    createEmployees,
    updateEmployee
}