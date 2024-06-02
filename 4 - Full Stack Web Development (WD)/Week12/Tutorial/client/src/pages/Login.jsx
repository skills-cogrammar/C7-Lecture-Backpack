import { useState } from "react";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("/login", {
        method: "POST",
        body: JSON.stringify({
          username,
          password,
        }),
        headers: {
          "Content-type": "application/json",
        },
      });

      const data = await response.json();
      
      localStorage.setItem("token", data.token)
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        name="username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />

      <input
        name="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <button> Login </button>
    </form>
  );
};

export default Login;