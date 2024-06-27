const express = require('express');
const bodyparser = require('body-parser');
const jwt = require('jsonwebtoken');
require('dotenv').config();

const app = express();

app.use(bodyparser.json());


app.get('/login', (req, res) => {
    const { username, password } = req.body;
    if (username === 'admin' && password === 'admin') {
        const payload = {
            username,
            admin: false
        }

        const token = jwt.sign(payload, process.env.SECRET_KEY, { 'expiresIn': '1h' });
        res.json({ token });
    } else {
        res.status(403).send({ error: "Incorrect username or password!" })
    }
});

app.get('/resource', (req, res) => {
    try {
        const token = req.headers["authorization"].split(' ')[1];
        console.log(token);
        const decoded = jwt.verify(token, process.env.SECRET_KEY);
        res.send(`Hello ${decoded.username}! Your JSON web token has been verified!`)
    } catch (error) {
        res.status(401).send({ error: 'INVALID JWT' });
    }
});



app.listen(8000, ()=> console.log('Server running on http://localhost:8000'));