const express = require("express");
const mongoose = require("mongoose");
const { routes } = require("./routes/routes");
const app = express();

app.use(express.json());

//Mongoose connectionn with Mongodb
const uri =
  "mongodb+srv://danw:Samaritan@cluster0.gmkkgcz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";

const clientOptions = {
  serverApi: { version: "1", strict: false, deprecationErrors: true },
};

mongoose
  .connect(uri, clientOptions)
  .then(() => {
    console.log("MongoDB connected Successfully");
  })
  .catch((err) => {
    console.log("Error connecting to mongodb", err);
  });

//Express Application server

app.listen(8000, () => {
  console.log("Server is running on http://localhost:8000");
});

app.use(routes);
