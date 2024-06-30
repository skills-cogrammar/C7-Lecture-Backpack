const TourModel = require("../models/tour.model");

exports.createTour = async (req, res) => {
    /*
        If we weren't using mongoose or a similar tool
        We would need to validate the input before creating the object 
        But mongoose already has these features for us and we wil make use of them
        in the next session 
    */

    try{
        // We expect the caller to pass something in the body that wioll match 
        // our model. If it doesn't then we will get an error that we can handle        
        const newTour = await TourModel.create(req.body);

        // We don't usually send the whole object since the client side 
        // already has the data. we might just send the id or something
        res.status(203).json(newTour)
    } catch(err){
        console.log(err);

        res.status(400).json({message: "Error creating object"})
    }    
}

exports.getAllTours = async (req, res) =>  {
    /**
     * Get all of the tours if there are no filters
     * Search for tours based on the filters applied
     * Set a default length to the result
     */

    try {
        // Find with no argumenst will return all of the values in the 
        // database table
        const tours = await TourModel.find(); 

        res.status(200).json(tours)
    } catch(err){
        // There needs to be a layer of abstraction between the error 
        // Message that is generated and the error message that is shown to the user 
        console.log(err)

        res.status(400).json({message: "Unable to fetch tours"})
    }
}

exports.getTour = async (req, res) => {
    /**
     * Assuming the path names are written in a complimentary way, there should be no
     * chance of this function being called if the ID isn't there
     */

    const id = req.params.id

    try{
        const tour = TourModel.findById(id);
        res.status(200).json(tour);
    } catch(err){
        console.log(err);

        // There is no way that the users input can cause an error
        // we can assume that any errors encoutered will be with the database engine
        res.status(500).json({message: "Server side error"})
    }
}