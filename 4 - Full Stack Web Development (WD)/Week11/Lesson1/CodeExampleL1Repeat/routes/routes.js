const controllers = require("../controllers/controllers");
const express = require("express");

const routes = express.Router();
routes.post("/create", controllers.createPerson);

module.exports = {
    routes
};