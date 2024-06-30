const { createEvent, updateEvent } = require("../repository/event.repository");

/*
    This controller is a lot more scaleable, we are not directly working with 
    the database.

    If we needed to change databases, all we would need to do is create a repo
    file that handles interactions with the new database and change the module 
    that is being imported in the first line.
*/


exports.createEvent = async (req, res, next) => {
    // The response we get will already have error handling taken care of 
    // so we know that we are either getting a success or fail message 
    const response = await createEvent(req.body);   

    // Based on the message we get, we will either send a success message 
    // or use the next to take use to the error message.
    if (response.success){
        res.status(203).json({message: "Created event", eventId: response})       
    } else{
        next(response.error)
    }
        
}

exports.updateEvent = async (req, res, next) => {
    // Get the ID from the query params and add it 
    // to the values that will be passed to the updateEvent function
    const id = req.params.id;
    const body = req.body;
    body.id = id;

    console.log(body)

    const response = await updateEvent(body);

    if (response.success){
        res.status(203).json({message: "Updated event", event: response.data})
    } else{
        next(response.error)    
    }
}