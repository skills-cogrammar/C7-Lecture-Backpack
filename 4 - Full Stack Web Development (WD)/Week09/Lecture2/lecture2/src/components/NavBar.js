import { Link } from "react-router-dom"

const NavBar = ()=>{

    const users = [
        { 
            id: 1,
            name: 'user1',
            role: 'Frontend Engineer'
        },
        {
            id: 2,
            name: 'user2',
            role: 'Backend Engineer'            
        },
        {
            id: 3,
            name: 'user3',
            role: 'Data scientist'
        }
    ]


    return (
        <nav>
            <Link to='/'>Home</Link>
            <Link to='/about'>About</Link>
            {
                users.map((user)=>{
                    return (
                        <Link to={`/user/${user.id}`} state={user}>User {user.id}</Link>
                    )
                })
            }
        </nav>
    )
}

export default NavBar