import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import App from "./App";
import {createBrowserRouter, RouterProvider} from "react-router-dom";
import Login from "./login/login";
import Banco from "./IndexBanco/banco";

const router = createBrowserRouter([
    {path: "/", element:<App/>},
    {path: "/", element:<Login/>},
    {path: "/banco", element:<Banco/>},
])
const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
      <RouterProvider router={router}/>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals(console.log);
