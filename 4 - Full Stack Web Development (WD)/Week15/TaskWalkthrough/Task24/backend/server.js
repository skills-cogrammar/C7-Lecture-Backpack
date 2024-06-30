const express = require('express')
const cors = require('cors')

const app = express();
app.use(cors());


app.get('/api/data', (req, res) => {
    res.json({message: "I know who I am, do you?"})
})

app.get('/api/custom', (req, res) => {
    res.json({message: "This is a custom message from your favourite programming language!"})
})

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`)
})