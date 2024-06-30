const { ApolloServer, gql } = require('apollo-server-express')
const express = require("express")
const app = express()
const cors = require("cors")
app.use(cors())

//schema
const typeDefs = gql`
    type Query {
        user: User
    }
        
    type User {
        name: String
        role: String
        hello: String
        age: Float
    }
`
//resolver
const resolvers = {
    Query: {
        user: ()=>({
            name: "Dan",
            role: "Programming Lecturer"
        })
    }
}

const server = new ApolloServer({ typeDefs, resolvers })
server.start().then(res=> {
    server.applyMiddleware({ app })
    app.listen(8000, ()=>{

        console.log(`Server is running http://localhost:8000${server.graphqlPath}`)
    })
})