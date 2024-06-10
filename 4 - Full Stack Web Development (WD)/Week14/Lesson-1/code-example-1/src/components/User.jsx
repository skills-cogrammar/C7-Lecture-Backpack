import { useContext } from "react"
import { UserContext } from "../context/userContext"

const User = ()=>{
    const { userData, handleChange } = useContext(UserContext)
    console.log("User Rerendered")
    return (
        <div>
            <button onClick={handleChange}>Change user</button>
            { userData.name }<br></br>
            { userData.role }<br></br>
            { userData.email }
        </div>
    )
}

export default User