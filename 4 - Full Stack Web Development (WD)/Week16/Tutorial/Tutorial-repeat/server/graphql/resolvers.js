const { EmployeeModel } = require("../models/employee")

const resolvers =  {
    Query: {
        hello: ()=> "Hello World",
        employees: async ()=> await EmployeeModel.find()
    },
    Mutation: {
        create: async (parent, args)=>{
            const { name, email, role, lineManager } = args

            if (name && email && role && lineManager ) {
                const newEmployee = new EmployeeModel({
                    name,
                    email,
                    role, 
                    lineManager
                })
                await newEmployee.save()
                return newEmployee
            } else {
                console.log("Error in creating employee")
            }
        },
        update: async (parent, args)=>{
            const { id } = args
            const updatedEmployee = await EmployeeModel.findByIdAndUpdate(id, args)
            if (!updatedEmployee) {
                console.log("Error in updating the employee")
            }
            return updatedEmployee
        },
        deleteEmployee: async (parent, args)=>{
            const { id } = args
            const deletedEmployee = await EmployeeModel.findByIdAndDelete(id)
            return deletedEmployee
        }
    }
}

module.exports = {
    resolvers
}