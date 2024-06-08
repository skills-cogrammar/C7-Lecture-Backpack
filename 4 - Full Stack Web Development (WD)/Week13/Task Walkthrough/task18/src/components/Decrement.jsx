const Decrement = ({ decrement })=>{
    return (
        <>
        <button onClick={()=>decrement("1000")} className="bg-orange-500 text-white p-4 cursor-pointer rounded-lg">Decrement</button>
        </>
    )
}

export default Decrement