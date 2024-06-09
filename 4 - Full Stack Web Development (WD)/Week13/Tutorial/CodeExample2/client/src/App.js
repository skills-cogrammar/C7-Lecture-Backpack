import useFetch from "./hooks/useFetch";
import Home from "./components/Home";

function App() {
  const { data, loading } = useFetch("http://localhost:8000/books")

  if (loading) {
    return <h1>Loading...</h1>
  }

  return (
    <div className="w-full flex flex-wrap gap-4">
      {data.books.map((book) => {
        return (
          <div key={book._id} className="w-[20vw] h-[20vh] flex flex-col">
            <p>Title: {book.title} </p>
            <p>Author: {book.author}</p>
            <p>GBP{book.price}</p>
            <div className="w-full h-1/2">
              <img src={book.image} alt={book.title} className="w-full object-contain h-full" />
            </div>
          </div>
        );
      })}
      <Home/>
    </div>
  );
}

export default App;
