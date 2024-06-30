const { gql } = require("apollo-server-express");

const typeDefs = gql`
    type Query {
        hello: String
        employees: [Employee]
        employee(id: ID): Employee
    }

    type Employee {
        id: ID
        name: String
        email: String
        role: String
        lineManager: String
    }

    type Mutation {
        create(name: String, email: String, role: String, lineManager: String): Employee
        update(id: ID, name: String, email: String, role: String, lineManager: String): Employee
        deleteEmployee(id: ID): Employee
    }
`

module.exports = {
    typeDefs
}