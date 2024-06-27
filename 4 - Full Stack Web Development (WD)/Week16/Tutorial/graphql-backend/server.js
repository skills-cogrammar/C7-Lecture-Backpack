const { ApolloServer, gql, PubSub } = require('apollo-server-express');
const { createServer } = require('http');
const express = require('express');
const { execute, subscribe } = require('graphql');
const { SubscriptionServer } = require('subscriptions-transport-ws');

const pubsub = new PubSub();
const MESSAGE_UPDATED = 'MESSAGE_UPDATED';

let message = "Hello, world!";

const typeDefs = gql`
  type Query {
    getMessage: String
  }
  type Mutation {
    updateMessage(newMessage: String!): String
  }
  type Subscription {
    messageUpdated: String
  }
`;

const resolvers = {
  Query: {
    getMessage: () => message,
  },
  Mutation: {
    updateMessage: (_, { newMessage }) => {
      message = newMessage;
      pubsub.publish(MESSAGE_UPDATED, { messageUpdated: message });
      return message;
    },
  },
  Subscription: {
    messageUpdated: {
      subscribe: () => pubsub.asyncIterator([MESSAGE_UPDATED])
    },
  },
};

const app = express();
const httpServer = createServer(app);

const server = new ApolloServer({
  typeDefs,
  resolvers,
  plugins: [{
    async serverWillStart() {
      return {
        async drainServer() {
          subscriptionServer.close();
        }
      };
    }
  }]
});

server.start().then(res => {
  server.applyMiddleware({ app });

  const subscriptionServer = SubscriptionServer.create({
    execute,
    subscribe,
    schema: server.schema,
  }, {
    server: httpServer,
    path: server.graphqlPath,
  });

  httpServer.listen(4000, () => 
    console.log(`Server ready at http://localhost:4000${server.graphqlPath}`)
  );
});
