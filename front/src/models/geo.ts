import type { Weather } from "./weather"

export type Info = {id: string, label: string, abstention: number, weather: Weather, weather_status: string}
export type Feature = { geometry: { type: "Polygon", coordinates: number[][][] }, properties: Info, type: "Feature" }
 
