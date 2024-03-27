import { useEffect, useRef } from "react";
import { useGeoJSON } from "../lib/d3.tsx";
import json from "../assets/csvjson.json";

const MapChart = () => {
    // const geoJSOn : {"type": string, "features": {geometry: {type: "Polygon", coordinates: number[][][]}, properties: any, type: "Feature"}[]} = {
    //     "type": "FeatureCollection",
    //   "features": []
    // }
    //     for(const el of json) {
    //         geoJSOn.features.push({
    //             "type": "Feature",
    //             "geometry": {
    //                 type: "Polygon",
    //                 coordinates: el.geo_shape.coordinates,
    //             },
    //             "properties": {
    //                 "name": el.Commune,
    //                 "population": el.Population,
    //             }})
    //     }
    //     console.log("geojson", geoJSOn);
    // const {geoJSON} = useGeoJSON();
    // const rep = useRef<JSX.Element[]>([])
    // useEffect(() => {
    //     rep.current.push(...addPath(geoJSON))
    // }, [geoJSON])
    const {paths, destroy} = useGeoJSON(json);
    // console.log(geoJSON);
    
    return (
        <>
        <div className="container">
            <svg width="500" height="500"> {paths} </svg>
        </div>
        <button onClick={() => destroy()}>Destroy</button>

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