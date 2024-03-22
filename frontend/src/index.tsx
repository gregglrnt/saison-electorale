import React from 'react'
import { createRoot } from 'react-dom/client'
import { StrictMode } from 'react';
import { BrowserRouter } from 'react-router-dom';
import App from './App.tsx'
import './style/index.css'
import './style/topBar.css'
import './style/searchBar.css'

const rootElement = document.getElementById('root');
createRoot(rootElement!).render(
    <StrictMode>
        <App />
    </StrictMode>
);

