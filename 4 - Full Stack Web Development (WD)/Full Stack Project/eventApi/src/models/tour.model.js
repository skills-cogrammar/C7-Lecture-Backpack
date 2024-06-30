const mongoose = require("mongoose");

const tourSchema = mongoose.Schema({
    title: String,
    subtitle: String,
    shortDescription: String,
    longDescription: String,
    promoterId: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "User"
    },
    eventIds: {
        type: [mongoose.Schema.Types.ObjectId],
        ref: "Event",
        default: []
    }
});

module.exports = mongoose.model("Tour", tourSchema); 
