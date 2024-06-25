const express = require("express")
const {getHelloWorld, getEmployees, createEmployees, updateEmployee} = require("../controllers/controllers")
const routes = express.Router()



//READ(R)
routes.get('/', getHelloWorld)
routes.get('/employees',getEmployees)
routes.post('/employees/create', createEmployees)
routes.put('/employees/update/:id', updateEmployee)

module.exports = {
    routes
}