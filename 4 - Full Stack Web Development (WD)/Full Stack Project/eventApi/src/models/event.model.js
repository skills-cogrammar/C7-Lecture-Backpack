const mongoose = require("mongoose");

const eventSchema = mongoose.Schema({
    location: String,
    dates: {
        type: [mongoose.Schema.Types.ObjectId],
        ref: "Date",
        default: []
    }
});

module.exports = mongoose.model("Event", eventSchema);