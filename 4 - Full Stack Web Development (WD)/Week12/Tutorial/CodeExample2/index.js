const express = require("express");
const mongoose = require("mongoose");
const { routes } = require("./routes/routes");
const cors = require('cors')
const app = express();

app.use(express.json());
app.use(cors())

//Mongoose connectionn with Mongodb
const uri = "mongodb://localhost:27017/tutorial";
  // "mongodb+srv://danw:Samaritan@cluster0.gmkkgcz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";

mongoose.connect(uri, { useNewUrlParser: true })
.then(() => {
  console.log("Connected to database");
})
.catch((err) => {
  console.log("Error connecting to database", err);
});

//Express Application server

app.listen(8000, () => {
  console.log("Server is running on http://localhost:8000");
});

app.use(routes);
