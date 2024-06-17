import { Link, useNavigate } from "react-router-dom"
import { useContext } from "react"
import { AuthContext } from "../context/AuthContext"

const NavBar = ()=>{
    const { token } = useContext(AuthContext)
    const navigate = useNavigate()

    const handleLogout = ()=>{
        localStorage.removeItem("token")
        navigate("/login")
    }
    return (
        <nav>
            <Link to='/'>Home</Link>
            {
                token ? <button onClick={handleLogout}>Logout</button> : <Link to='/login'>Login</Link>
            }
            <Link to='/register'>Register</Link>
        </nav>
    )
}

export default NavBar