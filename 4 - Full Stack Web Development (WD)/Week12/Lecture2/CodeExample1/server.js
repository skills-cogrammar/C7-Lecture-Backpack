const express = require('express');
const jwt = require('jsonwebtoken');

const app = express();
app.use(express.json());

app.post('/admin_login', (req, res) => {
    //const {username, password} = req.body;
    // Here we would check if the user details are in the database

    const payload = {
        "name": "Zahra",
        "password": "P@$$word",
        "admin": true
    };
    const token = jwt.sign(JSON.stringify(payload),
                           "lecture-1-secret",
                           {algorithm: 'HS256'});

    res.send({
        message: "Admin Login Successful",
        token: token
    });
    
});

app.get('/admin_resource', (req, res) => {
    const headers = req.headers['authorization'];
    const token = headers.split(' ')[1];

    try {
      const decoded = jwt.verify(token, 'lecture-1-secret');

      if (decoded.admin) {
        res.send({
            "message": "Success!" 
        });
      } else {
        res.status(403).send({
            "message": "Your JWT was verified, but you do not have admin access."
        });
      }
    } catch (e) {
      res.sendStatus(401);
    }
});

app.listen(8000, () => {
    console.log(`Server running on port 8000`);
});
  