const express = require('express');
const app = express();

let facts = [{id: 0, fact: "I have a rabbit"}, 
{id: 1, fact: "I am 23 years old"}, 
{id: 2, fact: "I studied Physics"}, 
{id: 3, fact: "I live in Cape Town"}
];

// CRUD Operations
// Create
app.put("/facts", (req, res) => {
    const fact = req.body;
    const factItem = {id: facts.length+1, fact: fact};
    facts.push(factItem);
    res.status(201).send(factItem);
});

// Update
app.put("/facts/:id", (req, res) => {
    const id = parseInt(req.params.id);
    const i = facts.findIndex((fact) => fact.id == id);
    
    if (i == -1){
        res.status(404).send("Fact not found!");
    } else {
        facts[i] = {...facts[i], ...req.body};
        res.send(facts[i]);
    }
});

// Delete
app.delete("/facts/:id", (req, res) => {
    const id = parseInt(req.params.id);
    const i = facts.findIndex((fact) => fact.id == id);
    
    if (i == -1){
        res.status(404).send("Fact not found!");
    } else {
        facts[i] = facts.splice(i, 1);
        res.send(facts[i]);
    }
})

// Static middleware
app.use(express.static('public'));

// Routes
// (Read)
app.get('/', function (req, res){
    let num = Math.floor(Math.random()*facts.length);
    res.send(facts[num]);
});

// Set up server
app.listen(8000, () => console.log("Listening on port 8000"));