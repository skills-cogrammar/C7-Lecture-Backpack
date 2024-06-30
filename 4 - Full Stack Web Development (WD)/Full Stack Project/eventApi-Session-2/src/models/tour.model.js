const mongoose = require("mongoose");

/*
    Mongoose includes a feature that allows us to reference other 
    documents by setting the type of the field to the ID of the document 
    and using the 'ref' attribute to state which table we want to link to.
    When getting the object, we can use the 'populate' method to show the actual 
    values stored in the document that we are referencing.

    MongoDB does not support this feature natively, it's an additional function added 
    by mongoose.

*/

const tourSchema = mongoose.Schema({
    title: {
        type: String,
        required: [true, "Tour must have a title"],
        maxLength: 50,
        minLength: 1    
    },
    subtitle: {
        type: String,
        maxLength: 50
    },
    shortDescription: {
        type: String,
        required: [true, "Tour must have a short description"],
        maxLength: 250,
        minLength: 30
    },
    longDescription: {
        type: String,
        required: [true, "Tour must have a long description"],
        maxLength: 500,
        minLength: 100
    },
    promoter: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "User"
    },
    eventIds: {
        type: [mongoose.Schema.Types.ObjectId],
        ref: "Event"
    }
});

module.exports = mongoose.model("Tour", tourSchema);