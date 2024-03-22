import { Election } from './Election'

export type Commune = {
    zip: string,
    code: string,
    insee_code: string,
    departement: string,
    label: string,
    centroid: string,
    Results: Results[]
}

export type Results = {
    communeId: string,
    commune: Commune,
    ballot: Election,
    ballotId: number,
    abstention: number,
    voters: number,
    invalidVotes: number
};