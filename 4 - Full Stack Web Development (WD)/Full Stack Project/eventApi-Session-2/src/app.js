const express = require("express");
const mongoose = require("mongoose");
const helmet = require("helmet")
const rateLimit = require("express-rate-limit")
const errorHandler = require("./middleware/error.middleware");

/*
  Express is built around middleware. Everything that we pass as
  app.use() is a piece of middleware that will be executed in the background.

  The order that we pass our middleware is really important as express runs the middleware
  in the order that it is defined. So if we have a piece of middleware that needs to be applied for
  all of the endpoints, it needs to be added as soon as possible.

*/


// rate limiting can be added to lmit the number of requests a user 
// can make in a specified amout of time 
// This is a good way to protect again DDoS attacks 
// and can also be used as a 'fair us' approach to ensure that no 
// one user is overusing resources and making it slower for everyone else
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 10, // limit each IP to 100 requests per windowMs
  message: "Too many requests, please try again later."
})

const app = express();
// helmet adds some security headers that will protect against 
// common attacks like cross site scripting and others
app.use(helmet()) 

// Passing the limiter here will ensure that the rate limit applies to all
// of the endpoints in our application.
app.use(limiter)

app.use(express.json());

// We can conect to the database here, but this limits our ability to 
// connect to other databases
//
// A better approach would be to create a class for the app which takes in 
// a database connection so that we can dynamically change our database without 
// having to come into the app.js file.
mongoose.connect("mongodb://localhost:27017/mern-auth", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
}).then(() => console.log("connected"))
.catch(() => console.log("Not connected"));


// We can add the routes to the different endpoints here 
const authRouter = require("./routes/auth.route")
const eventsRouter = require("./routes/events.route")
app.use("/auth", authRouter)
app.use("/events", eventsRouter)

// The error handling endpoint needs to come after the other endpoints
// so that it can be accessed by any outer endpoint that calls next()
app.use(errorHandler);

module.exports = app;