// Import and initialise express
const express = require('express');
const app = express();

// Allow json to be parsed
app.use(express.json());

// Create To Do List API
let todoList = [{id: 1, title: "Chore", description: "Wash the dishes"}];

// Routing 
// Create (POST)
app.post("/todos", (req, res) => {
    console.log(req.body);

    let title = req.body.title;
    let description = req.body.description;

    let item = {id: todoList.length+1, title, description, completed: false};
    todoList.push(item);

    res.status(201).send(item);
});

// Read (GET)
app.get("/todos", (req, res) => {
    res.send(todoList);
});

// Update (PUT)
app.put("/todos/:id", (req, res) => {
    let id = parseInt(req.params.id);
    let i = todoList.findIndex((item) => {item.id == id});

    if (i == -1) {
        res.status(404).send("Item not found");
    } else {
        todoList[i] = {...todoList[i], ...req.body};
        res.send(todoList[i]);
    }
});

// Delete
app.delete("/todos/:id", (req, res) => {
    let id = parseInt(req.params.id);
    let i = todoList.findIndex((item) => {item.id == id});

    if (i == -1) {
        res.status(404).send("Item not found");
    } else {
        let removed = todoList.splice(i, 1);
        res.send(removed);
    }
});

// Create our server
app.listen(8000, () => { 
    console.log("Server running, listening on port 8000")
});



