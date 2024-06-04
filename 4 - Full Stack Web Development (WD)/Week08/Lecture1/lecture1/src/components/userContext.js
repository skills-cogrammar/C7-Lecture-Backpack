import { createContext, useContext } from 'react';

const userContext = createContext("User");

export function useUserName () {
    return useContext(userContext);
}

export default userContext;