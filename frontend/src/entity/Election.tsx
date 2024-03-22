import { Results } from './Commune'

enum ElectionType {
    LEG,
    PRES,
    EURO,
    DEP,
    MUNI
};

export type Election = {
    id: number,
    date: Date,
    type: ElectionType,
    round: number,
    Result: Results[],
}