const express = require("express")
const app = express()
const cors = require("cors")
const {routes} = require('./routes/routes')

app.use(express.json())
app.use(cors())




app.use(routes)
app.listen(8000, ()=>{
    console.log("Server is running on http://localhost:8000")
})


