export type Meteo = {
    stationId: string,
    date: Date,
    wind_speed: number,
    temperature_kelvin: number,
    temperature_celsius: number,
    humidity: number,
    cloudiness: number,
    ice_height: number,
    rain: number,
    coordinates: string,
    commune: string,
    zip: string
}