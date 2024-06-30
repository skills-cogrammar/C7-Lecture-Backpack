const mongoose = require("mongoose")

const EmployeeSchema = new mongoose.Schema({
    name: String,
    email: String,
    role: String,
    lineManager: String
})

const EmployeeModel = mongoose.model('Emplyee', EmployeeSchema)

module.exports = {
    EmployeeModel
}