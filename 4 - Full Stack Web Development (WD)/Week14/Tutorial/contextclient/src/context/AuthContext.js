import { createContext, useEffect, useState } from "react";

const AuthContext = createContext(null)

const AuthProvider = ({ children })=>{
    const [ token, setToken ] = useState("")

    useEffect(()=>{

        setToken(localStorage.getItem("token"))

    }, [token])
    
    return (
        <AuthContext.Provider value={{ token }}>
            { children }
        </AuthContext.Provider>
    )
}

export {
    AuthContext,
    AuthProvider
}