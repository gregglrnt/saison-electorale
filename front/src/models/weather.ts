export type WeatherFromApi = Omit<Weather, "date"> & {
    date: string
} 

export type Weather = {
    cloudiness ?: number,
    date: Date,
    humidity ?: number,
    ice_height ?: number,
    rain ?: number,
    temperature_celsius?: number,
}

export type StationWithMeteoFromAPI = {
    commune: string,
    coordinates: string,
    id: string,
    zip: string,
    Meteo: WeatherFromApi[],
}