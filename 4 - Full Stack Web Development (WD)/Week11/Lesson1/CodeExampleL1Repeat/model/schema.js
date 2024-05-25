const mongoose = require("mongoose");

const personSchema = mongoose.Schema({
    name: {
        required: true,
        type: String
    },

    age: {
        required: true,
        type: Number
    }
});

const personModel = mongoose.model('Person', personSchema);

module.exports = {
    personModel
};
