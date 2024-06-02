import { useEffect, useState } from "react"

const Resource = () => {
    const [message, setMessage] = useState("");

    const fetchResource = async () => {
        const response = await fetch("/resource", {
            headers: {
                "Authorization": `Bearer ${localStorage.getItem("token")}`,
                "content-type": "application/json"
            }
        });

        console.log(response);

        const data = await response.json()
        console.log(data);
        setMessage(data.message);
    }

    useEffect(() => {
        fetchResource();
    }, []);

    return <div>{message}</div>
}

export default Resource;