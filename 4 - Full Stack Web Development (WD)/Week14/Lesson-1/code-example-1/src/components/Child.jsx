import User from "./User"

const Child = ()=>{
    console.log("Child Rerendered")
    return (
        <div>
            <User/>
        </div>
    )
}
export default Child