import useLocalStorage from "./hooks/useLocalStorage"
const Random = ()=>{
    const { value, setValue } = useLocalStorage("randomItems", [{
        random1: "Hello World"
    }])

    console.log(value)
    return (
        <h1>Hello World</h1>
    )
}

export default Random