const models = require('../models/BlogModel')
const BlogModel = models.BlogModel


const helloWorld = (req, res)=>{
    res.json({message: "Hello Hyperion"})
}

//C(Create)
const createBlogs = async (req, res)=>{
    const { title, content, author } = req.body
    const blog = await BlogModel.create({ //creates a blogs
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
    const blogs = await BlogModel.find() //finds all blogs
    res.json(blogs)
}

//U(update)
const updateBlog = async (req, res)=>{
    const { id } = req.params
    const values = req.body

    const blog = await BlogModel.findByIdAndUpdate(id, values)
    res.json({
        message: "Blog Updated successfully.",
        blog: blog
    })
}

//D(delete)
const deleteBlog = async (req, res)=>{
    const { id } = req.params 
    const blog = await BlogModel.findByIdAndDelete(id)

    res.json({
        message: "Blog deleted successfully",
        blog: blog
    })

}

module.exports = {
    helloWorld,
    readBlogs,
    createBlogs,
    updateBlog,
    deleteBlog
}