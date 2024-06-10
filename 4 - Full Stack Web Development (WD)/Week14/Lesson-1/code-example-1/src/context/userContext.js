import { createContext, useState } from "react";

//Create context or store
const UserContext = createContext(null);

//Provides the information in the store
const UserProvider = ({ children }) => {
  const [userData, setUser] = useState({
    name: "Dan",
    email: "danw@hyperiondev.com",
    role: "Programming Lecturer",
  });

  const handleChange = () => {
    setUser({
      name: "Bongani",
      email: "bongani@hyperiondev.com",
      role: "Programming Lecturer",
    });
  };

  return <UserContext.Provider value={{ userData, handleChange }}>{children}</UserContext.Provider>;
};

export { UserContext, UserProvider };
