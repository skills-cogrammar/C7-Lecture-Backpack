const express = require('express')
const controllers = require('../controllers/controller')

const routes = express.Router()

routes.get('/', controllers.helloWorld)
routes.get('/blogs', controllers.readBlogs)
routes.post('/blogs/create', controllers.createBlogs)

module.exports = {
    routes
}