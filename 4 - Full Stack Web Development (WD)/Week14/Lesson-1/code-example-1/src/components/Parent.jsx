import Child from "./Child"

const Parent = ({ userData })=>{
    console.log("Parent Rerendered")
    return (
        <div>
            <Child/>
        </div>
    )
}

export default Parent