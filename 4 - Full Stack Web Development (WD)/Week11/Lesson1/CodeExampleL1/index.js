const express = require('express')
const mongoose = require('mongoose')//mongoose import
const router = require('./routes/route')

const app = express()
app.use(express.json())




//MongoDB Connection
/**
 * @NOTE - Insert username and password accordingly
 */
const uri = "mongodb+srv://{username}:{password}@cluster0.2maadky.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";

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