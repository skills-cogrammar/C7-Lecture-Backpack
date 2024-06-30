const { ApolloServer, gql } = require('apollo-server-express');
const express = require('express');
const cors = require('cors');


// Define your schema here
const typeDefs = gql`
  type Query {
    hello: String
  }
`;

// Define your resolvers here
const resolvers = {
  Query: {
    hello: () => 'Hello, world!',
  },
};

// Create an instance of ApolloServer
const server = new ApolloServer({ typeDefs, resolvers });
app.use(cors());

const app = express();
server.start().then(res => {
  server.applyMiddleware({ app });

  app.listen({ port: 4000 }, () =>
    console.log(`Server ready at http://localhost:4000${server.graphqlPath}`)
  );
});
