//express init
const express = require("express")
const app = express()
const cors = require("cors")

//mongoose import
const mongoose = require("mongoose")

//gql imports
const { ApolloServer } = require("apollo-server-express")
const { typeDefs } = require("./graphql/typeDef") 
const { resolvers } = require('./graphql/resolvers')

//middleware
app.use(cors())

//mongoose connection
const uri = "mongodb+srv://danw:Samaritan@cluster0.gcz7jkl.mongodb.net/?appName=Cluster0";
const clientOptions = { serverApi: { version: '1', strict: true, deprecationErrors: true } };
mongoose.connect(uri, clientOptions)
.then(()=> console.log("DB connected successfully"))
.catch((err)=> console.log(err))

const server = new ApolloServer({typeDefs, resolvers})

server.start().then(res=> {
    server.applyMiddleware({ app })
    app.listen(8000, ()=>{

        console.log(`Server is running http://localhost:8000${server.graphqlPath}`)
    })
})