//Schema (Structure of the document in the MongoDB)
const mongoose = require("mongoose")

const BookSchema = new mongoose.Schema({
    title: {
        type: String,
        required: true
    },
    author: {
        type: String,
        required: true
    },
    price: Number,
    image: String,
    created_at: {
        type: Date,
        default: Date.now //It auto creates the date immediately
    }
})

const Book = mongoose.model("Book", BookSchema)


module.exports = {
    Book
}