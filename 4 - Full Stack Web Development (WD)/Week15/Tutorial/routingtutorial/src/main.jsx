import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './pages/App.jsx'
import './index.css'
import About from "./pages/About.jsx"
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import ProductDetail from './pages/ProductDetail.jsx'
import Error from './pages/Error.jsx'

//create the paths in your application
const paths = createBrowserRouter([
  {
    path: "/",
    element: <App/>,
    errorElement: <Error/>
  },
  {
    path: "/about",
    element: <About/>
  },
  {
    path: "/product/:id",
    element: <ProductDetail/>
  }
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={paths} />
  </React.StrictMode>,
)
