import type { Election } from "$lib/election"
import type { Weather } from "./weather"

export type ResultWeather =  {
    election: Election,
    results: Result,
    weather: Weather[]
}

export type CommuneWithResult = {
    commune: Commune,
    electionWeather: ResultWeather[],
    //Results: Result[]
    //closer_station: StationWithMeteo
}

export type Result =  {
        abstention: number,
        voters: number,
        invalidVotes: number,
}

export type Commune = {
    zip: string,
    code: string,
    departement: string,
    label: string,
    centroid: string,
    geojson: string,
}