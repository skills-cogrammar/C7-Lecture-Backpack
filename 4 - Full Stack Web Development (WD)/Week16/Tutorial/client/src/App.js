import { useQuery, useMutation, useSubscription, gql } from '@apollo/client';

const GET_MESSAGE = gql`
  query GetMessage {
    getMessage
  }
`;

const UPDATE_MESSAGE = gql`
  mutation UpdateMessage($newMessage: String!) {
    updateMessage(newMessage: $newMessage)
  }
`;

const MESSAGE_SUBSCRIPTION = gql`
  subscription {
    messageUpdated
  }
`;

function App() {
  const { data, loading } = useQuery(GET_MESSAGE);
  const [updateMessage] = useMutation(UPDATE_MESSAGE);
  useSubscription(MESSAGE_SUBSCRIPTION, {
    onSubscriptionData: ({ subscriptionData }) => {
      alert("Message updated: " + subscriptionData.data.messageUpdated);
    }
  });

  if (loading) return <p>Loading...</p>;
  if (!data) return <p>No data found</p>;

  return (
    <div>
      <p>{data.getMessage}</p>
      <button onClick={() => updateMessage({ variables: { newMessage: "Hello from Apollo Client!" } })}>
        Update Message
      </button>
    </div>
  );
}

export default App;
