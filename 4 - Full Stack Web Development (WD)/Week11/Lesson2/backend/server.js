// Imports
const express = require("express");
const cors = require("cors");

// Create express app
const app = express();

// Configure cors
app.use(cors());

// Create get route listener for frontend
app.get('/api/data', (req, res) => {
    const data = {message: "Hello from the backend :)"};
    res.json(data);
})

// Create the server
const PORT = process.env.PORT || 8000;

app.listen(PORT, () => {
    console.log(`Backend server is now running on port ${PORT}.`);
})