const mongoose = require("mongoose")


const employeeSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    role: {
        type: String,
    },
    joined_at: {
        type: Date,
        default: Date.now
    }
})

const Employee = mongoose.model('Employee', employeeSchema)

module.exports = {
    Employee
}