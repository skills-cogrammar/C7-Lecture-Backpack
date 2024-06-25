import useFetch from "../hooks/useFetch"

const Home = ()=>{
    const { data, loading } = useFetch("http://localhost:8000/") 

    if ( loading ) {
        return <h1>Loading...</h1>
    }
    return (
        <div>
            <h1>{ data.message}</h1>
        </div>
    )
}
export default Home
