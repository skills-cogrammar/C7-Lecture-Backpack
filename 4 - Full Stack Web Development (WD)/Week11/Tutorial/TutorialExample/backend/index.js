const express = require('express')
const mongoose = require('mongoose')//mongoose import
const router = require('./routes/route')
const cors = require("cors")

//Initializa an express
const app = express()
//JSON middleware to accept json objects from request
app.use(express.json())
app.use(cors())




//MongoDB Connection
/**
 * @NOTE - Insert username and password accordingly
 */
const username = process.env.MONGO_USER
const password = process.env.MONGO_PASSWORD

const uri = `mongodb+srv://${username}:${password}@cluster0.fhgaqrt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0`;
console.log(uri)

const clientOptions = { serverApi: { version: '1', strict: true, deprecationErrors: true } };

mongoose.connect(uri, clientOptions)
.then(()=>{
    console.log('Connection to mongodb done successfully...')
})
.catch((error)=>{
    console.log('Error connecting to mongodb', error)
})


//Nodejs and Express Server
app.use('/', router.routes)
app.listen(8000, ()=>{
    console.log('Server is running on port http://localhost:8000')
})