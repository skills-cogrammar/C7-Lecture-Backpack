const mongoose = require('mongoose')

const blogSchema = mongoose.Schema({
    title: String,
    content: String,
    author: String,
    createdAt: {
        type: Date,
        default: Date.now
    }
})

const BlogModel = mongoose.model('Blog', blogSchema)

module.exports = {
    BlogModel
}