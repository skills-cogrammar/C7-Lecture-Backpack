import { useState } from "react";

const Register = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [admin, setAdmin] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
        const response = await fetch("/create/user", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ username, password, admin }),
          });

        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.log(error);
    }
  };


  return (
    <form onSubmit={handleSubmit}>
        <input type="text" placeholder="username" onChange={(e) => setUsername(e.target.value)} />
        <input type="password" placeholder="password" onChange={(e) => setPassword(e.target.value)} />
        
        <select onChange={(e) => setAdmin(e.target.value)} value={admin}>
            <option value={false}>Normal User</option>
            <option value={true}>Admin</option>
        </select>

        <button type="submit">Register</button>
    </form>
  )
};

export default Register;