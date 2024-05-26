const express = require("express")
const cors = require("cors")
const app = express()

app.use(cors())

const listItems = [
    {
        name: "Dan",
        stack: "MERN"
    },
    {
        name: "Bongani",
        stack: "MEAN"
    },
    {
        name: "Zahra",
        stack: "MEAN"
    },
    {
        name: "Elon",
        stack: "MERN"
    }
]

app.get('/api/', (req, res)=>{
    res.json({
        message: "Data from backend",
        people: listItems
    })
})

app.get('/api/meanstack', (req, res)=>{
    const meanStackPeople = listItems.filter((person)=> person.stack === "MEAN")
    res.json({
        message: "The response contains people the MEAN stack",
        people: meanStackPeople
    })
})

app.get('/api/mernstack', (req, res)=>{
    const mernStackPeople = listItems.filter((person)=> person.stack === "MERN")
    res.json({
        message: "The response contains people the MERN stack",
        people: mernStackPeople
    })
})

app.listen(8000, ()=>{
    console.log("Server is running on http://localhost:8000")
})