const EventModel = require("../models/event.model");

async function createEvent(eventBody){
    // Input validation would usually be done here before 
    // writing to the database, but since we're working with 
    // mongoose, we can skip this step 
    // https://joi.dev/api/?v=17.13.3

    try{
        const event = await EventModel.create(eventBody);
        return {success: true, id: event._id}
    } catch(error){        
        error.status = 400;
        return {success: false, error: error}
    }        
}

async function updateEvent(eventBody){
    const { id, location } = eventBody;

    try{
        const event = await EventModel.findById(id);   
        event.location = location;
        event.save()        

        return {success: true, data: event}
    } catch(error){
        error.status = 400;
        return {success: false, error: error}
    }
}

module.exports = {
    createEvent,
    updateEvent
}