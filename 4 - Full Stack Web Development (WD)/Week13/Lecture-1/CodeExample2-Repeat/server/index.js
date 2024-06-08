//Entry File of our app
const express = require("express");
const app = express();
const mongoose = require("mongoose")
const cors = require("cors")
const { routes } = require("./routes/routes");

app.use(cors())//Allowed access to all origins
app.use(express.json())

const uri = "mongodb+srv://danw:Samaritan@cluster0.olgyhca.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";
const clientOptions = { serverApi: { version: '1', strict: true, deprecationErrors: true } };

mongoose.connect(uri, clientOptions)
.then(()=>console.log("Connection to database was successful"))
.catch((error)=>console.log("Error connecting to db", error.errorResponse.errmsg))

app.use(routes);
app.listen(8000, function () {
  console.log("Server is running on http://localhost:8000");
});
