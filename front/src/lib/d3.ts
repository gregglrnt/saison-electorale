import * as d3 from "d3"
import { writable } from "svelte/store"
import type { DataFromCommunes } from "../models/data"
import type { Feature } from "../models/geo"
import type { PathType } from "../models/path"






const transformToGeoJson = (json: DataFromCommunes[]) : {"type": "FeatureCollection", "features": Feature[]} => {
    const features : Feature[] = []
    for (const el of json) {
        const geojson = JSON.parse(el.geojson)
        features.push({
            type: "Feature",
            geometry: {
                type: "Polygon",
                coordinates: geojson.coordinates,
            },
            properties: {
                id: el.code,
                label: el.commune,
                abstention: el.abstention,
                weather: el.weather_status,
            }
        })
    }
    return {
        "type": "FeatureCollection",
        "features": features,
    }
}
export const paths = writable<PathType[]>([])

export let element : SVGSVGElement & HTMLElement;

export type DataFromAPI = {
    communes: DataFromCommunes[],
    election: {
        date: Date,
        id: number,
        round: number,
        type: string
    },
    page: number,
}
export const generatePathsFromSource = (json: DataFromAPI | undefined) => {
    if(!json) return;
    const colorScale = d3.scaleDiverging(d3.interpolateSpectral).domain([100, 0])
    const geopath = d3.geoPath().projection(d3.geoConicConformal().center([-1.454071, 48.279229]).scale(4000).translate([300, 300]));
    const geojson = transformToGeoJson(json.communes);
    return geojson.features.map((feature) : void => {
        try {
            const color = feature.properties.abstention ? colorScale(feature.properties.abstention) : 'lightgray';
            paths.update((previousPaths) => {
                previousPaths.push({
                    ...feature.properties,
                    d: geopath(feature),
                    fill: color,
                })
                return previousPaths
            })
        } catch( error) {
            console.log(`error in ${feature}`, error)
        }
})
}