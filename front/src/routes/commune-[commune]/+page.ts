import { env } from "$env/dynamic/public";
import type { DataFromCommune } from "../../models/data";
import type { CommuneWithResult } from "../../models/results";
import type { PageLoad } from "./$types"
import {parseElection} from "$lib/election"
import { parseWeather } from "$lib/weather";

const isSameDay = (s1: string | Date, s2: string | Date) => {
    const d1 = new Date(s1);
    const d2 = new Date(s2);
    return d1.getFullYear() == d2.getFullYear() && d1.getMonth() === d2.getMonth() && d1.getDate() === d2.getDate();
}

const parseSingleCommuneData = (json : DataFromCommune) : CommuneWithResult => {
    const {Results, closer_station,...commune} = json;
    const results = []
    for (const res of Results) {
        const weather = closer_station.Meteo.filter((weather) => isSameDay(weather.date, res.ballot.date))
        results.push({
            election: parseElection(res.ballot),
            results: res,
            weather: parseWeather(weather)

        })
    }
    return {
        commune: commune,
        electionWeather: results,

    }
}

export const load : PageLoad = async ({fetch, params}) : Promise<CommuneWithResult> => {
    return await fetch(`${env.PUBLIC_BACKEND_URL}/commune/${params.commune}/results`).then(res => res.json()).then((json) => parseSingleCommuneData(json));
}