const express = require('express')
const controllers = require('../controllers/controller')

const routes = express.Router()

//All API routes defined here
routes.get('/', controllers.helloWorld)
routes.get('/blogs', controllers.readBlogs)
routes.post('/blogs/create', controllers.createBlogs)
routes.put('/blogs/update/:id', controllers.updateBlog)
routes.delete('/blogs/delete/:id', controllers.deleteBlog)

module.exports = {
    routes
}