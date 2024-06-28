const EventModel = require("../models/event.model");
const TourModel = require("../models/tour.model");

exports.createEvent = async (req, res) => {
    /**
     * The events will be used from the tour route
     * We need to get the tour ID along with the event details since an event has to be 
     * part of a tour
     */

    const tourId = req.params.tourId;

    try{
        // Create a new event
        const event = await EventModel.create(req.body);
        const eventId  = event._Id;

        // Link the new event to a tour
        const tour = await TourModel.findById(tourId);                
        tour.eventIds.push(eventId);
        tour.save();

        res.status(203).json(event)        
    }catch(err) {
        console.log(err)
        res.status(500).json(err)
    }
}

exports.getAllEvents = async (req, res) => {
    try {
        const events = await EventModel.find();
        res.status(200).json(events)
    } catch(err){
        console.log(err);

        res.status(500).json({message: "Unable to connect to server"})
    }
}


// We can add some query params to this function to make it a bit more dynamic
exports.getEvent = async (req, res) => {
    try {
        const events = await EventModel.find()
        // res.status(200).json(events)
        return events
    } catch(err){
        console.log(err);

        // res.status(500).json({message: "Unable to connect to server"})
        return {message: "Unable to connect to server"}
    }
}