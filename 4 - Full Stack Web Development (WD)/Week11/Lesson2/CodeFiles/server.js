// Import the packages that we'll be using 
const express = require('express');
const cors = require('cors');

// Create a new express app
const app = express();

// Enable Cross-Origin Resource Sharing
app.use(cors());

// Define the route for the frontend to retrieve messages
app.get('/api/data', (req, res) => {
  const data = { message: 'Hello from the back end!' };
  res.json(data); // Send data as a response
});


// Define the port number for the server 
// Check if the environmental variable is defined
// If not, use port 5000
const PORT = process.env.PORT || 5000;

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
