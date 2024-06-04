import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [author, setAuthor] = useState("");

  const [blogs, setBlogs] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    console.log(title, content, author);

    const response = await fetch("http://localhost:8000/blogs/create", {
      method: "POST",
      body: JSON.stringify({ title, content, author }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    const info = await response.json();
    console.log(info);
  };

  const fetchBlogs = async () => {
    const response = await fetch("http://localhost:8000/blogs");
    const data = await response.json();
    setBlogs(data);
  };

  const handleDelete = async (id) => {
    const response = await fetch(`http://localhost:8000/blogs/delete/${id}`, {
      method: "DELETE",
    });
    const data = await response.json();

    alert("Blog has been deleted", data);
  };

  const handleUpdate = async (id)=>{

    console.log(title, content, author);

    const response = await fetch(`http://localhost:8000/blogs/update/${id}`, {
      method: "PUT",
      body: JSON.stringify({ title, content, author }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    const info = await response.json();
    console.log(info);
    alert("Blog Updated Successfully")

  }

  useEffect(() => {
    fetchBlogs();
  }, []);

  return (
    <div className="App">
      <h1>Create Form</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="title"
          value={title}
          placeholder="Title"
          onChange={(e) => setTitle(e.target.value)}
        />
        <input
          type="text"
          name="content"
          value={content}
          placeholder="Content"
          onChange={(e) => setContent(e.target.value)}
        />
        <input
          type="text"
          name="author"
          value={author}
          placeholder="Author"
          onChange={(e) => setAuthor(e.target.value)}
        />
        <button type="submit">Submit</button>
      </form>
      {blogs.map((blog) => {
        return (
          <div key={blog._id}>
            <h1>{blog.title}</h1>
            <button onClick={() => handleDelete(blog._id)}>Delete</button>

            <form onSubmit={(e)=>e.preventDefault()}>
              <input
                type="text"
                name="title"
                value={title}
                placeholder="Title"
                onChange={(e) => setTitle(e.target.value)}
              />
              <input
                type="text"
                name="content"
                value={content}
                placeholder="Content"
                onChange={(e) => setContent(e.target.value)}
              />
              <input
                type="text"
                name="author"
                value={author}
                placeholder="Author"
                onChange={(e) => setAuthor(e.target.value)}
              />
              <button onClick={()=>handleUpdate(blog._id)} type="submit">Submit</button>
            </form>
          </div>
        );
      })}
    </div>
  );
}

export default App;
