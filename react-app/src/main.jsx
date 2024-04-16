import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './components/App/App.jsx'
import './index.css'
import {createBrowserRouter, RouterProvider} from "react-router-dom";
import RootLayout from "./routes/RootLayout/RootLayout.jsx";
import FrontPage from "./routes/FrontPage/FrontPage.jsx";
import DownloadPage from "./routes/DownloadPage/DownloadPage.jsx";
import ProcessPage from "./routes/ProcessPage/ProcessPage.jsx";


const router = createBrowserRouter([
    {path: '/', element: <RootLayout/>, children: [
            {path: "/home", element: <FrontPage/>},
            {path: "/download", element: <DownloadPage/>},
            {path: "/process", element: <ProcessPage/>}
        ]}
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router}></RouterProvider>
  </React.StrictMode>,
)
