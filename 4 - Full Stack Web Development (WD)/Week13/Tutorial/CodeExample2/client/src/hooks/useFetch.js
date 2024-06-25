import { useState, useEffect } from "react";

const useFetch = (url)=>{
    const [ data, setData ] = useState(null)
    const [ loading, setLoading ] = useState(true) 

    const fetchData = async ()=>{
        setLoading(true)
        try {
            const response = await fetch(url)
            const data = await response.json()
            setData(data)
        } catch(error) {
            console.log(error)
        }
        setLoading(false)
    }

    useEffect(()=>{
        fetchData()

    }, [url])


    return {
        data,
        loading
    }

}


export default useFetch