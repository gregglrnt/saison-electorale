import { writable } from "svelte/store";
import type { DataFromAPI } from "./map";
import type { Weather } from "../models/weather";

export type Point = {
    weather: Weather,
    weather_status: string,
    label: string,
    temperature: number,
    rain: number,
    abstention: number,
}

export const points = writable<Point[]>([])

export const definePointsDefault = ( json : DataFromAPI) => {
    json.communes.map((commune) => {
        points.update((previousPoints) => {
            if(!commune.weather || !commune.abstention) return previousPoints;
            if(commune.weather.rain && commune.weather.rain < 0) return previousPoints;
            previousPoints.push({
                weather: commune.weather,
                label: commune.commune,
                rain: commune.weather.rain || 0,
                temperature: commune.weather.temperature_celsius || 0,
                abstention: commune.abstention,
                weather_status: commune.weather_status,
            })
            return previousPoints;
        })
    })
}