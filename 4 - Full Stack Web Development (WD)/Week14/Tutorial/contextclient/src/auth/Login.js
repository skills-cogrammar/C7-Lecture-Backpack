import { useState } from "react";
import NavBar from "../components/NavBar";
import { useNavigate } from "react-router-dom";

const Login = () => {
    const [ email, setEmail ] = useState("")
    const [ password, setPassword ] = useState("")
    const navigate = useNavigate()

    const handleLogin = async(e)=>{
        e.preventDefault()

        const response = await fetch("http://localhost:8000/api/auth/login", {
            method: "POST",
            headers: {
                "Content-Type" : "application/json"
            },
            body: JSON.stringify({
                email: email,
                password: password
            })

        })
        const data = await response.json()

        localStorage.setItem("token", data.token)
a
        navigate("/")
    }

  return (
    <>
      <NavBar />
      <form onSubmit={handleLogin}>
        <input onChange={(e)=>setEmail(e.target.value)} name="email" type="text" placeholder="Enter email" />
        <input onChange={(e)=>setPassword(e.target.value)} name="password" type="password" placeholder="Enter password." />
        <button>Submit</button>
      </form>
    </>
  );
};

export default Login;
