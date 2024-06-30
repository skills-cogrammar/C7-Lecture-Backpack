const mongoose = require("mongoose");

const ticketSchema = mongoose.Schema({
    price: Number,
    type: String
});

const dateSchema = mongoose.Schema({
    date: {
        type: Date,
        required: true
    },
    venue: {
        type: String,
        required: true
    },
    tickets: [ticketSchema]
});

module.exports = mongoose.model("Date", dateSchema);