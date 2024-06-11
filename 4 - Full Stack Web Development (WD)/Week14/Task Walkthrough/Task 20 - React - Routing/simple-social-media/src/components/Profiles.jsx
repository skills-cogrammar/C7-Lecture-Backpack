import { Link } from "react-router-dom";

const Profiles = () => {
    const profiles = [
        {
            id: 1,
            name: "John Doe"
        },
        {
            id: 2,
            name: "Jane Doe"
        },
        {
            id: 3,
            name: "June Doe"
        },
        {
            id: 4,
            name: "Jack Doe"
        }
    ]

    return (
        <div>
            <h2>These are the profiles of your friends:</h2>
            {
                profiles.map((profile) => (
                    <li key={profile.id}>
                        <Link to={`/profile/${profile.id}`}>{ profile.name }</Link>
                    </li>
                ))
            }
        </div>
    )
}

export default Profiles;