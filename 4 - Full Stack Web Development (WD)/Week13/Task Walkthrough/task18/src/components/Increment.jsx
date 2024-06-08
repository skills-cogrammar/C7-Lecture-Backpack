const Increment = ({ increment })=>{
    return (
        <>
        <button onClick={()=>increment("1000")} className="flex-shrink-0 text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg mt-10 sm:mt-0">Increment</button>

        </>
    )
}

export default Increment