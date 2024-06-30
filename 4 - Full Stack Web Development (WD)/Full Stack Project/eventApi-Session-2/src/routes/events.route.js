const router = require("express").Router();
const {verifyJwt ,verifyAdmin } = require("../middleware/jwt.middleware");
const { createEvent, updateEvent }  = require("../controllers/event.controller");

/*
    We can make sure that only admin users can create events 
    by passing our middleware 

    In the express router, everything after the endpoint route will be middleware.
    Middleware that contains the next argument should be passed before middleware 
    that does not have the next argument as we will not be able to run the next piece of 
    middleware.

    If the next() is not called, the other middleware will also not be run, this will 
    help us in authorization as we can skip the business logic part if the user is not
    logged in and is not an admin.
*/
router.post("/",verifyJwt, verifyAdmin, createEvent);
router.put("/:id", verifyJwt, verifyAdmin, updateEvent)


module.exports = router;