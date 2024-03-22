import React, { useEffect } from 'react'
import L from 'leaflet'

const MapChart = () => {
    useEffect(() => {
        const script = document.createElement('script');
        script.src = '../graph-script.js';
        script.async = true;

        document.body.appendChild(script);

        return () => {
            document.body.removeChild(script);
        }
    },[]);
    
    return (
        <>
        <div className="container">
            <canvas id="myChart"></canvas>
        </div>

        </>
    )
    /*useEffect(() => {
        const map = L.map('map').setView([46.227638, 2.213749], 4);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        }).addTo(map);

        L.geoJson()
    },[])*/
}

export default MapChart