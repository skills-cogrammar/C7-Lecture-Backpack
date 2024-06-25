import { Link } from "react-router-dom"

const NavBar = ()=>{
    return (
        <nav>
            <Link to='/'>Home</Link>
            <Link to='/about'>About</Link>
            <Link to='/nested'>Nested</Link>
        </nav>
    )
}
export default NavBar  