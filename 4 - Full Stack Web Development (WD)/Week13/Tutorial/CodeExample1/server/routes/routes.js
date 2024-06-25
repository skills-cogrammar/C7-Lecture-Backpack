const express = require("express")
const { helloController } = require('../controllers/controller')
const mongoose = require("mongoose")
const routes = express.Router()

const uri = "mongodb+srv://danw:Samaritan@cluster0.wtrt4eg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";
const clientOptions = { serverApi: { version: '1', strict: true, deprecationErrors: true } };


mongoose.connect(uri, clientOptions)
.then(()=>console.log("Connection to mongodb successfull."))
.catch((err)=>console.log(err))

routes.get('/', helloController)

module.exports = {
    routes
}