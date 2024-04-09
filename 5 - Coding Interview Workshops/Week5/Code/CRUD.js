var mysql = require('mysql2');

// Connect to the mySQL server 
// Replace the username and password with your details
var connection = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "CoGrammar123",
    database: "exampleJSDatabase"
});

// Use the following to delete the table if you already ran the code
// let clear = "DROP TABLE crew"
// connection.connect (function (err) { 
//     if (err)
//         throw err;
//     console.log("Connected to mySQL Server");  
//     connection.query(clear, function(err, result) {
//         if (err)
//             throw err; 
//     })
// });

// Create the Table
let createTable = `CREATE TABLE crew (crewID INT AUTO_INCREMENT PRIMARY KEY, 
    firstName VARCHAR(255), lastName VARCHAR(255), roomNumber INT)`
connection.connect (function (err) { 
    if (err)
        throw err;
    console.log("Connected to mySQL Server");  
    connection.query(createTable, function(err, result) {
        if (err)
            throw err;
        console.log("Table created"); 
    })
});

// Add entries to the table
let insertInto = "INSERT INTO crew (firstName, lastName, roomNumber) VALUES ?"
let rows = [
    ["Zahra", "Mohamed", 7],
    ["Moumita", "Aich", 12]
]
connection.connect (function (err) { 
    if (err)
        throw err;
    console.log("Connected to mySQL Server");  
    connection.query(insertInto, [rows], function(err, result) {
        if (err)
            throw err;
        console.log(result.affectedRows + " row(s) inserted."); 
    })
});


// Retrieve entries from the table
let selectAll = "SELECT * FROM crew"
connection.connect (function (err) { 
    if (err)
        throw err;
    console.log("Connected to mySQL Server");  
    connection.query(selectAll, function(err, result, fields) {
        if (err)
            throw err;
        console.log(result); 
    })
});


let selectCondition = "SELECT firstName FROM crew WHERE roomNumber = 7"
connection.connect (function (err) { 
    if (err)
        throw err;
    console.log("Connected to mySQL Server");  
    connection.query(selectCondition, function(err, result, fields) {
        if (err)
            throw err;
        console.log(result); 
    })
});

// Update entries in the table
let updateEntry = "UPDATE crew SET roomNumber = 6 WHERE firstName = 'Moumita'"
connection.connect (function (err) { 
    if (err)
        throw err;
    console.log("Connected to mySQL Server");  
    connection.query(updateEntry, function(err, result) {
        if (err)
            throw err;
        console.log(result.affectedRows + " row(s) updated."); 
    })
});

// Delete entries from the table
let deleteEntries = "DELETE FROM crew WHERE crewID = 2"
connection.connect (function (err) { 
    if (err)
        throw err;
    console.log("Connected to mySQL Server");  
    connection.query(deleteEntries, function(err, result) {
        if (err)
            throw err;
        console.log(result.affectedRows + " row(s) deleted."); 
    })
});

