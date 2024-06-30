const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors")

const app = express();

app.use(express.json());
app.use(cors())


const MONGO_URI = process.env.MONGO_URI

mongoose.connect(MONGO_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    dbName: "eventsApi"
})
.then(() => console.log("MongoDB connected"))
.catch(err => console.log(err));

// Endpoints 
const tourRoutes = require("./routes/tour.route");
app.use("/tours", tourRoutes);

module.exports = app;