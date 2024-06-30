const mongoose = require("mongoose");

const userSchema = mongoose.Schema({
    authId: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "Auth"
    },
    fullName: {
        type: String,
        required: true,
        minLength: 5,
        maxLength: 30,
        match: [/^[a-zA-Z0-9]+$/, 'is invalid']
    },
    email: {
        type: String,
        required: true,
        unique: true,
        match: [/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(.\w{2,3})+$/, 'Please fill a valid email address']
    },
    eventsLiked: {
        type: Array,
        default: []
    },
    eventsCreated: {
        type: Array,
        default: []
    }    
})

module.exports = mongoose.model("User", userSchema);