import type { Weather, WeatherFromApi } from "../models/weather";
import { mostFrequent } from "./utils";

export const parseWeather = (weather: WeatherFromApi[]) : Weather[] => {
    return weather.map((meteo => { return {...meteo, date: new Date(meteo.date)}}))
}

export const medianTemperature = (weather : Weather[]) => {
    return (weather.reduce((a, b) => a + (b.temperature_celsius || a), 0) / weather.length).toFixed(1)
}

export const getClimate = (w: Weather) => {
        if(w.rain && w.rain > 0.1) return "🌧️"
        if(w.ice_height && w.ice_height > 1) return "❄️";
        if(w.cloudiness && w.cloudiness > 50) return "☁️";
        return "☀️";
    }

export const getGlobalClimate = (weather: Weather[]) => {
    const climates : string[] = [];
    weather.forEach((w) =>  {
        climates.push(getClimate(w));
    })    
    return mostFrequent(climates);
}