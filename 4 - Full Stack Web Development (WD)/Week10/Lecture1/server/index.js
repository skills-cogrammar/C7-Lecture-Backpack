let express = require('express')
let app = express()

let todos = [
    {
        id: 1,
        title: 'Wash dishes'
    },
    {
        id: 1,
        title: 'Sleep'
    }
]


app.get('/todos', function(req, res) {
    res.send(todos)
})

app.listen(8000, function() {
    console.log('Server is running on http://localhost:8000')
})