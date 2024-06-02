import { useEffect, useState } from "react"

const UpdateUser = () => {
    const [id, setId] = useState("") 
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [admin, setAdmin] = useState(false)

    useEffect(() => {
        
        const fetchUserData = async() => {
            const response = await fetch("/user", {
                headers: {
                    "Authorization": `Bearer ${localStorage.getItem("token")}`,
                    "content-type": "application/json"
                }
            });
            const data = await response.json();            

            setId(data.data.id)
            setUsername(data.data.username)
            setPassword(data.data.password)
            setAdmin(data.data.admin)
            console.log(data)
        }
        fetchUserData();    
        
    }, [])

    const handleSubmit = async (e) => {
        e.preventDefault();
    
        try {
            const response = await fetch(`/update/user/${id}`, {
                method: "PUT",
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
        <input value={username} type="text" placeholder="username" onChange={(e) => setUsername(e.target.value)} />
        <input value={password} placeholder="password" onChange={(e) => setPassword(e.target.value)} />
        
        <select onChange={(e) => setAdmin(e.target.value)} value={admin}>
            <option value={false}>Normal User</option>
            <option value={true}>Admin</option>
        </select>

        <button type="submit">Update</button>
    </form>
    )
}

export default UpdateUser;