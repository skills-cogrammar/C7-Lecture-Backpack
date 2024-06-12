var mysql = require('mysql2');

// Connect to the mySQL server 
// Replace the username and password with your details
var connection = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "CoGrammar123"
});

// To connect to the server you have to define 
// functions to handle any errors
// All queries and statements need to be done wrapped within the 
// connect function
var create = "CREATE DATABASE exampleJSDatabase"

connection.connect (function (err) { 
    if (err)
        throw err;
    console.log("Connected to mySQL Server");  
    connection.query(create, function(err, result) {
        if (err)
            throw err;
        console.log("Database created"); 
    })
});

