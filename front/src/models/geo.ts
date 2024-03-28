export type Info = {id: string, label: string, abstention: number, weather: string}
export type Feature = { geometry: { type: "Polygon", coordinates: number[][][] }, properties: Info, type: "Feature" }
 
