import { createContext, useState } from "react";

const ThemeContext = createContext(null)

const ThemeProvider = ({ children })=>{

    const [ theme, setTheme ] = useState("light")

    const handleTheme = ()=>{
        setTheme(theme === "light" ? "dark" : "light")
    }

    const changeColor = {
        width: "100vw",
        height: "100vh",
        backgroundColor: theme === "light" ? "white" : "black",
        color: theme === "light" ? "black" : "white"
    }

    return (
        <ThemeContext.Provider value={{theme, handleTheme, changeColor}}>
            { children }
        </ThemeContext.Provider>
    )
}

export {
    ThemeContext,
    ThemeProvider
}