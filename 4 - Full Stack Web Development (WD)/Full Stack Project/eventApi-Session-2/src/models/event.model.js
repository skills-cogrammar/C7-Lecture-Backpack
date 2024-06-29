const mongoose = require("mongoose");

const eventSchema = mongoose.Schema({    
    location: {
        type: String,
        required: [true, "location is required"],
        minLength: [3, "location must be at least 3 characters long"],
        maxLength: [50, "location must be at most 50 characters long"]
    },
    dates: {
        type: [mongoose.Schema.Types.ObjectId],
        ref: "Date"
    }
});

module.exports = mongoose.model("Event", eventSchema);