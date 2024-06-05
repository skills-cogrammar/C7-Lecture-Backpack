const mongoose = require('mongoose');

const EmployeeSchema = new mongoose.Schema({
  name: String,
  position: String,
  office: String,
  salary: Number,
});

const Employee = mongoose.model('Employee', EmployeeSchema);

module.exports = Employee;
