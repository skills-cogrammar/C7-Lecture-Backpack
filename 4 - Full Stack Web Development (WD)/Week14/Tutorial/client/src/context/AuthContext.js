import React, { createContext, useContext, useState } from 'react';
import axios from 'axios';

const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);

    const login = async (email, password) => {
        try {
            const response = await axios.post('http://localhost:5000/api/auth/login', { email, password });
            setUser(response.data);
        } catch (error) {
            console.error('Login failed:', error);
        }
    };

    const register = async (username, email, password) => {
        try {
            const response = await axios.post('http://localhost:5000/api/auth/register', { username, email, password });
            console.log('Registration successful', response.data);
        } catch (error) {
            console.error('Registration failed:', error);
        }
    };

    const logout = () => {
        setUser(null);
    };

    return (
        <AuthContext.Provider value={{ user, login, register, logout }}>
            {children}
        </AuthContext.Provider>
    );
};
