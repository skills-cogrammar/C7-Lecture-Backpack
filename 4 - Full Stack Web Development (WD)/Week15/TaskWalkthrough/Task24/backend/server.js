const express = require('express')
const cors = require('cors')

const app = express();
app.use(cors());


app.get('/api/data', (req, res) => {
    res.json({message: "Hello from the back end team!"})
})

app.get('/api/custom', (req, res) => {
    res.json({message: "This is a custom message from your AI!"})
})

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`)
})