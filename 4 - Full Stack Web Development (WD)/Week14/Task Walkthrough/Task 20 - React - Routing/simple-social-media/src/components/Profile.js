import { useParams } from "react-router-dom";

const Profile = () => {

    const profiles = {
        1: { id: 1, name:'John Doe', bio: 'John Loves Food!'},
        2: { id: 2, name:'Jane Doe', bio: 'Jane Loves Travelling!'},
        3: { id: 3, name:'June Doe', bio: 'John Loves Politics!'},
        4: { id: 4, name:'Jack Doe', bio: 'Jack Loves All Trades!'}
    }

    let { id } = useParams();

    const profile = profiles[id]

    return (
        <div>
            <h1>{profile.name}</h1>
            <p>{ profile.bio }</p>
        </div>
    )
}

export default Profile;