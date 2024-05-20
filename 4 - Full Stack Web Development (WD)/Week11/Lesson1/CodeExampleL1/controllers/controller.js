const models = require('../models/BlogModel')
const BlogModel = models.BlogModel


const helloWorld = (req, res)=>{
    res.json({message: "Hello Hyperion"})
}

//C(Create)
const createBlogs = async (req, res)=>{
    const { title, content, author } = req.body
    const blog = await BlogModel.create({
        title: title,
        content: content,
        author: author
    })
    const savedBlog = await blog.save()
    res.json({
        message: "Blog saved successfully",
        savedBlog: savedBlog
    })

}

//R(read)
const readBlogs = async (req, res)=>{
    const blogs = await BlogModel.find()
    res.json(blogs)
}

module.exports = {
    helloWorld,
    readBlogs,
    createBlogs
}