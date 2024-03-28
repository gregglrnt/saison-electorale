import type { Weather } from "./weather";

export type DataFromCommunes = {
    code: string,
    geojson: string,
    commune: string,
    centroid: string,
    abstention: number,
    weather_status: string,
    weather: Weather[],
}