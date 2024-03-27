import { useEffect, useState } from "react"
import * as  d3 from "d3"


type Feature = { geometry: { type: "Polygon", coordinates: number[][][] }, properties: any, type: "Feature" }
type GeoJSON = {type: string, features: Feature[]}

const transformToGeoJson = (json: any) : GeoJSON => {
    const features : Feature[] = []
    for (const el of json) {
        features.push({
            type: "Feature",
            geometry: {
                type: "Polygon",
                coordinates: el.geo_shape.coordinates,
            },
            properties: {
                name: el.Commune,
                population: el.Population
            }
        })
    }
    return {
        "type": "FeatureCollection",
        "features": features,
    }
}

export const useGeoJSON = (json: any) => {
    const [r, setR] = useState<JSX.Element[]>([])
    useEffect(() => {
        const geojson = transformToGeoJson(json);
        setR(addPath(geojson))
    }, [json])
    return {paths: r, destroy: () => setR([])};
}


export const addPath = (geojson: GeoJSON) => {
    const colorScale = d3.scaleThreshold<number, string>().domain([0.1, 0.5, 1, 1.5, 2, 10, 100]).range(d3.schemeBlues[7])
    const geopath = d3.geoPath().projection(d3.geoConicConformal().center([2.454071, 46.279229]).scale(3000).translate([300, 300]));
        return geojson.features.map((shape, n) => {
            try {
                const color = shape.properties.population ? colorScale(shape.properties.population) : 'lightgray'
                return <path id={shape.properties.name} key={n} d={geopath(shape)} stroke="lightgrey" strokeWidth={0.5} fill={color} onMouseEnter={() => console.log(shape.properties.name)}/>
            } catch (error) {
                console.log(`error in ${n}`, shape, error)
                return <></>
            }
            })       
}