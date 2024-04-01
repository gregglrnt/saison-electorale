export type Weather = {
    cloudiness ?: number,
    date: Date,
    humidity ?: number,
    ice_height ?: number,
    rain ?: number,
    temperature_celsius?: number,
}

export type StationWithMeteo = {
    commune: string,
    coordinates: string,
    id: string,
    zip: string,
    Meteo: Weather[],
}