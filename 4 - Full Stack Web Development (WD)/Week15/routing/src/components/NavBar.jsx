import { Link } from "react-router-dom"
import Contact from "../pages/Contact"

const Navbar = ()=>{
    return (
        <nav> 
            <Link to='/'>Homes</Link>
            <Link to='/about'>About</Link>
            <Link to='/contact'>Contact</Link>
        </nav>
    )
}

export default Navbar