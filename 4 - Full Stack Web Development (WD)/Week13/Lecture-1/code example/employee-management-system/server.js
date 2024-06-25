const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
require('dotenv').config();
const employeesRouter = require('./routes/employee')


const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json()); // Allows us to receive JSON in requests
app.use('/employees', employeesRouter)

// MongoDB connection
mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected successfully'))
  .catch(err => console.log(err));


app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
