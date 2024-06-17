import { createContext, useState } from "react";

//create the store
const ThemeContext = createContext(null)

//create the provider
const ThemeProvider = ({ children })=>{

    //state logic of dark/light theme
    const [ theme, setTheme ] = useState("light") //the initial theme when the page renders is light theme

    const handleTheme = ()=>{
        setTheme(theme === "light" ? "dark": "light") //if theme is light change to dark and vise versa
    }

    const currentBackground = {
        backgroundColor: theme === "light" ? "white" : "black",
        color: theme === "light" ? "black" : "white",
        width: "100vw",
        height: "100vh"
    }

    return (
        <ThemeContext.Provider value={{ theme, handleTheme, currentBackground}}>
            { children }
        </ThemeContext.Provider>
    )
}


//exports
export {
    ThemeProvider,
    ThemeContext
}