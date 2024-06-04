const express = require('express')
const { getHomePath, getAllUsers, createUser, loginUser, resource } = require('../controllers/controller')


const routes = express.Router()

//Home path = http://localhost:8000/
routes.get('/', getHomePath)
routes.get('/users', getAllUsers)
routes.post('/create/user', createUser)
routes.post('/login', loginUser)
routes.get('/resource', resource)

module.exports = {
    routes
}