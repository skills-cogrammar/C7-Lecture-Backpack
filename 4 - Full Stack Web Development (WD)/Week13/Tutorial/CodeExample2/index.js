const express = require("express")
const app = express()
const cors = require("cors")
const mongoose = require("mongoose")
const { routes } = require("./routes/routes")

app.use(express.json())
app.use(cors())
//MVC 
//Models
//Views (Replaced by our React app)
//Controllers

const uri = "mongodb+srv://danw:Samaritan@cluster0.w3trbyz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";
const clientOptions = { serverApi: { version: '1', strict: true, deprecationErrors: true } };

mongoose.connect(uri,clientOptions)
.then(()=>console.log("Connection to mongoDB was successfull"))
.catch((error)=>console.log("Error connecting to DB", error))



app.use(routes)
app.listen(8000, ()=>{
    console.log("Server is running on http://localhost:8000")
})