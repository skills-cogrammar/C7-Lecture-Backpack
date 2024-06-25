import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './pages/App.jsx'
import './index.css'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import About from './pages/About.jsx'
import ProductDetail from './pages/ProductDetail.jsx'
import Nested from './pages/Nested.jsx'

//initialize the paths
const paths = createBrowserRouter([
  {
    //home path(Where the user lands)
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
  },
  {
    path: "/nested",
    element: <Nested/>,
    children: [
      {
        path: "/nested/:id",
        element: <ProductDetail/>
      }
    ]
  }
])


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={paths} />
  </React.StrictMode>,
)
