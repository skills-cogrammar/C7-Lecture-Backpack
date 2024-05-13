import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

//pages
import App from './pages/App';
import Users from './pages/Users';
import User from './pages/User';

import reportWebVitals from './reportWebVitals';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

const paths = createBrowserRouter([
  {
    path: '/',
    element: <App/>
  },
  {
    path: '/users',
    element: <Users/>
  },
  {
    path: '/user/:userId',
    element: <User/>
  }
])



const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={paths}/>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
