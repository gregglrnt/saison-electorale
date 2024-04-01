import { env } from "$env/dynamic/public";
import { writable } from "svelte/store";

export const currentElection = writable<string>();

export type ElectionFromAPI = {
    type: string,
    round: number,
    date: string,
}

export type Election = {
    date: Date,
    label: string,
    value: string,
}

export const elections = writable<Election[]>([])

const getElectionType = (election: ElectionFromAPI) : string => {
    switch(election.type) {
        case "LEG": return "législatives 🔴";
        case "DEP": return "départementales 🟠";
        case "PRES" : return "présidentielles 🔵";
        case "MUNI" : return "municipales 🟣";
        case "EURO": return "européennes ⭐";
        case "REG": return "régionales 🟤";
    }
    return ""
}

export const parseElection = (election: ElectionFromAPI) : Election => {
    const label = (election.round == 1 ? "1er" : "2e") + " tour des " + getElectionType(election) + " " + election.date.split("-")[0];
    const date = new Date(election.date);
    return {
        label,
        date,
        value: election.date.split("T")[0]
    }
}

export const parseElections = (elections: ElectionFromAPI[]) : Election[] => {
    return elections.map((election) => {
        return parseElection(election);
})
}

export const getElections = async() => {
    fetch(`${env.PUBLIC_BACKEND_URL}/election/all`)
        .then((res) => res.json())
        .then((json: ElectionFromAPI[]) => {
            const allElections = parseElections(json);
            elections.set(allElections)
            currentElection.set(allElections[0].value)
        });
}