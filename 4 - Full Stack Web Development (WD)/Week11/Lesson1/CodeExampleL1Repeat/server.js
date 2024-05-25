const mongoose = require("mongoose");
const express = require("express");
const router = require("./routes/routes");
require("dotenv").config();

// Creating Express server
const app = express();
app.use(express.json());
app.use("/" ,router.routes);

const port = process.env.PORT || 8000;
app.listen(port, () => {
    console.log(`Server is running on port number ${port}.`)
});

// Connect to MongoDB
const URL = `mongodb+srv://new-user:xjLPIT7o5N5kjhGq@cogrammar.7rxh44z.mongodb.net/?retryWrites=true&w=majority&appName=CoGrammar`;
const clientOptions = {
    serverAPI: { version: '1', strict: true, deprecationErrors: true },
};

mongoose
 .connect(URL, clientOptions)
 .then(() => {
    console.log("Connected to MongoDB successfully....");
 })
 .catch((error) => {
    console.error("Error occured while connecting to the DB", error);
 });
