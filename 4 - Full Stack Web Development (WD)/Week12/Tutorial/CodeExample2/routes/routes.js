const express = require('express')
const { getHomePath, getAllUsers, createUser, loginUser, resource, getUser, updateUser } = require('../controllers/controller')


const routes = express.Router()

//Home path = http://localhost:8000/
routes.get('/', getHomePath)
routes.get('/users', getAllUsers)
routes.post('/create/user', createUser)
routes.post('/login', loginUser)
routes.get('/resource', resource)
routes.get('/user', getUser)
routes.put('/update/user/:id', updateUser)


module.exports = {
    routes
}