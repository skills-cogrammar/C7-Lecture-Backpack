import { useState } from "react";
import NavBar from "../components/NavBar";

const Register = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();
    const response = await fetch("http://localhost:8000/api/auth/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: username,
        email: email,
        password: password,
      }),
    });
    const data = await response.json();
    console.log(data);
  };

  return (
    <>
      <NavBar />
      <form onSubmit={handleRegister}>
        <input
          onChange={(e) => setUsername(e.target.value)}
          type="username"
          name="username"
          placeholder="Enter username"
        />
        <input
          onChange={(e) => setEmail(e.target.value)}
          type="email"
          name="email"
          placeholder="Enter email"
        />
        <input
          onChange={(e) => setPassword(e.target.value)}
          type="password"
          name="password"
          placeholder="Enter password"
        />
        <button>Submit</button>
      </form>
    </>
  );
};

export default Register;
