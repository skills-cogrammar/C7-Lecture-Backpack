const mongoose = require('mongoose')

const UserSchema =  mongoose.Schema({
    username: {
        type: String,
        unique: true
    },
    password: {
        type: String,
        required: true
    },
    admin: {
        type: Boolean //True or False
    }
})


const User = mongoose.model('Users', UserSchema)

module.exports = {
    User
}