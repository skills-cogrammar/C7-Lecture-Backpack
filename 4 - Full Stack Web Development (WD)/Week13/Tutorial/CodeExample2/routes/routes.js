const express = require("express")
const { getHomeController, getAllBooks, createBook, updateBook, deleteBook } = require("../controllers/controller")
const routes = express.Router()

routes.get('/', getHomeController)
routes.get('/books', getAllBooks)
routes.post('/books/create', createBook)
routes.put('/books/update/:id', updateBook)
routes.delete('/books/delete/:id', deleteBook)

module.exports = {
    routes
}