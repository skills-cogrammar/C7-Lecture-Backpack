import './App.css';
import { useQuery, gql } from '@apollo/client';


const GET_MESSAGE = gql`
  query GetMessage {
    hello
  }`

function App() {

  const { loading, error, data } = useQuery(GET_MESSAGE);

  console.log(data)

  if(loading) return <h2>Loading...</h2>
  if(error) return <h2>Error: </h2>

  return (
    <div className="App">
      <p>{ data.hello }</p>
    </div>
  );
}

export default App;
