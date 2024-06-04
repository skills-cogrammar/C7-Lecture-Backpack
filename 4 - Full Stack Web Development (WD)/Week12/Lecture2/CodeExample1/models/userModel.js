const mongoose = require('mongoose');

// Create Schema
const userSchema = mongoose.Schema({
    username: String,
    password: String,
    admin: Boolean
});

const userModel = mongoose.model("User", userSchema);

module.exports = {
    userModel
};