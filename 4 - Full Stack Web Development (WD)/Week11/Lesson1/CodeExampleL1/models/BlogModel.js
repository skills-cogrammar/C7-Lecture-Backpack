const mongoose = require('mongoose')

//structure/define a document
const blogSchema = mongoose.Schema({
    title: String,
    content: String,
    author: String,
    createdAt: {
        type: Date,
        default: Date.now //auto created
    }
})

const BlogModel = mongoose.model('Blog', blogSchema)

module.exports = {
    BlogModel
}