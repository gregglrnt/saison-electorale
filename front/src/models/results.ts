import type { Election } from "$lib/election"

export type CommuneWithResult = Commune & {
    Results: Result[]
}

export type Result =  {
        abstention: number,
        voters: number,
        invalidVotes: number,
        ballot: Election,
}

export type Commune = {
    zip: string,
    code: string,
    departement: string,
    label: string,
    centroid: string,
    geojson: string,
}