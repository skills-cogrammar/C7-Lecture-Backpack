import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

import reportWebVitals from './reportWebVitals';

import App from './pages/App';
import About from './pages/About';
import User from './pages/User';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

//create paths
const paths = createBrowserRouter([
  {
    path: '/',
    element: <App/>,
    errorElement: <h1>Error Page</h1>
  },
  {
    path: '/about',
    element: <About/>
  },
  {
    path: '/user/:userId',  //dynamic path /user/1 or /user/2
    element: <User/>
  }
])

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={paths} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
