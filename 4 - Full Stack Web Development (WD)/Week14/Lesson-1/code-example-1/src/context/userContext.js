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
      name: "John Doe",
      email: "johndoe@hyperiondev.com",
      role: "Software Lead",
    });
  };

  return <UserContext.Provider value={{ userData, handleChange }}>{children}</UserContext.Provider>;
};

export { UserContext, UserProvider };
