import { useLocation } from "react-router-dom"

const User = ()=>{
    const location = useLocation()
    const userData = location.state

    return (
        <div>
            <h1>{ userData.name } </h1>
        </div>
    )
}

export default User