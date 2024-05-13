import { useParams, useLocation } from "react-router-dom"
import NavBar from "../components/NavBar"

const User = ()=>{
    const { userId } = useParams()

    const location = useLocation()
    const userData = location.state
    
    return (
        <section>
            <NavBar/>
            <h1>User { userId} </h1>
            <p>Name: {userData.name} </p>
            <p>Role: {userData.role} </p>
        </section>
    )
}

export default User