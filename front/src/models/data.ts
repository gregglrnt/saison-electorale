import type { ElectionFromAPI } from "$lib/election";
import type { Commune, Result } from "./results";
import type { StationWithMeteoFromAPI, Weather } from "./weather";

export type DataFromCommunes = {
    code: string,
    geojson: string,
    commune: string,
    centroid: string,
    abstention: number,
    weather_status: string,
    weather: Weather,
}

export type ResultFromApi = Result & {ballot: ElectionFromAPI}

export type DataFromCommune = Commune & {
    Results: ResultFromApi[],
    closer_station: StationWithMeteoFromAPI,
}