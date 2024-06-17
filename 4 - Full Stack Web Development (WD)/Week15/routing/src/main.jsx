import React from 'react'
import ReactDOM from 'react-dom/client'
import App, { fetchCharacters } from './App.jsx'
import './index.css'
import { createBrowserRouter, Router, RouterProvider } from 'react-router-dom'
import About from './pages/About.jsx'
import Contact from './pages/Contact.jsx'
import Error from './pages/Error.jsx'

const routes = createBrowserRouter([
  {
    path: "/",
    element: <App/>,
    errorElement: <Error/>,
    loader: fetchCharacters,
    children: [
      {
        path: "contacts/:contactId",
        element: <Contact/>
      }
    ]
  },
  {
    path: "/about",
    element: <About/>,
  }

])
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={routes} />
  </React.StrictMode>,
)
