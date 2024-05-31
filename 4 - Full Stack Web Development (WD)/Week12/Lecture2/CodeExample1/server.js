const express = require('express');
const mongoose = require('mongoose');
const router = require('./routes/route');
// Import CORS for front end

const app = express();
app.use(express.json());

// MongoDB Connection
const url = "mongodb+srv://temp-user:1234@cogrammar.7rxh44z.mongodb.net/?retryWrites=true&w=majority&appName=CoGrammar"
const clientOptions = {
  serverApi: {
    version: "1",
    strict: true,
    deprecationErrors: true
  }
};
mongoose.connect(url, clientOptions)
  .then(() => {
    console.log("Connection to MongoDB successful!");
  })
  .catch((error) => {
    console.error("Error occured while connecting to the database.", error);
  })

app.use('/', router.router);
app.listen(8000, () => {
    console.log(`Server running on port 8000`);
});
  