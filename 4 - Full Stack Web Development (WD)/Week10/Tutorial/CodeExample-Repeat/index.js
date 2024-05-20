const express = require('express')
const app = express()

app.use(express.json())

let todos = [
    {
        id: 1,
        title: "Eat"
    }
]

app.get('/', (req, res)=>{
    res.json({message: "Hello World"})
})

//C(Create)
app.post('/todos/create', (req, res)=>{
    const { title } = req.body
    const todo = { id: todos.length + 1, title: title}
    todos.push(todo)
    res.status(201).json({message: "Created successfully."})

})



//R(read)
app.get('/todos', (req, res)=>{
    res.json(todos)
})

//U(Update)
app.put('/todo/update/:id', (req, res)=>{
    const id = parseInt(req.params.id)
    const todoIndex = todos.findIndex(todo=> todo.id === id)
    if (todoIndex === -1) {
        res.json({message : "Not found"})
    } else {
        todos[todoIndex] = {...todos[todoIndex], ...req.body}
        console.log(todos[todoIndex])
        res.json({message: "Updated"})
    }

})

//D(delete)
app.delete('/todo/delete/:id', (req, res)=>{
    const id = parseInt(req.params.id)
    const todoIndex = todos.findIndex(todo => todo.id === id)
    if (todoIndex === -1) {
        res.json({message: "Not found"})
    } else {
        const deleted = todos.splice(todoIndex, 1)
        res.json({message: "Item deleted"})
    }
})


app.use(express.static('public'))


// console.log(app)
app.listen(8000, ()=>{
    console.log("Server is running on port http://localhost:8000")
})