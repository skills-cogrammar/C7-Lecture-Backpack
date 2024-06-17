const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
require('dotenv').config();
const authRoutes = require('./routes/authRoutes')

const app = express();

app.use(cors());
app.use(express.json());
app.use('/api/auth', authRoutes);


app.listen(8000, () => console.log(`Server running on port http://localhost:8000`));

const uri = "mongodb+srv://danw:Samaritan@cluster0.vrj2mpt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";


mongoose.connect(uri).then(() => console.log('MongoDB connected!'))
    .catch(err => console.log(err))

