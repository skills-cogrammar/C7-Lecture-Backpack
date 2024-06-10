import Parent from "./Parent"

const GrandParent = ()=>{
    console.log("GrandParent Rerendered")
    return (
        <div>
            <Parent/>

        </div>
    )
}

export default GrandParent