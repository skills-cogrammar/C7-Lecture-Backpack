import { gql, useQuery } from "@apollo/client";

const GET_USER_NAME = gql`
  query GetUserRole {
    user {
      name
      role
      age
      hello
    }
  }
`;

function App() {
  const { loading, error, data } = useQuery(GET_USER_NAME);

  console.log(data);

  if (loading) return <h2>Loading...</h2>;
  if (error) return <h1>Error in fetching the info</h1>;

  return (
    <>
      {data.user.name}
      {data.user.role}
    </>
  );
}

export default App;
