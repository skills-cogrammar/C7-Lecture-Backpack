import { useEffect, useState, useRef } from "react"
import { Link } from "react-router-dom"

const Users = ()=>{
    const [ users, setUsers ] = useState([])
    const title = useRef(null)



    const fetchUsers = async ()=>{
        const response = await fetch('https://jsonplaceholder.typicode.com/users')
        const data = await response.json()
        console.log(data)
        setUsers(data)
        
    }

    useEffect(()=>{
        fetchUsers()
        title.current.style.color = 'yellow'
    }, [])

    return (
        <div>
            <h1 ref={title}>USERS</h1>
            {
                users.map((user)=>(
                    <div key={user.id}>
                        <h1>{ user.name }</h1>
                        <p>{ user.address.city }</p>
                        <Link to={`/user/${user.id}`} state={user}>Link to User</Link>
                    </div>
                ))
            }
        </div>
    )
}

export default Users