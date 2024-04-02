import { env } from "$env/dynamic/public";
import { paths, type DataFromAPI } from "./map"
import { points } from "./scatter";

export const fetchAndTransform = async (url: string, page: number = 0) => {
    const res = await fetch(`${env.PUBLIC_BACKEND_URL}/compare/all/${url}?page=${page}`)
    const json = await res.json()
    return json as DataFromAPI;
}

export const fetchAllPagesAnd = async (from: string, callback: (json: DataFromAPI) => void) => {
    if(from == undefined) return;
    paths.set([])
    points.set([])
    const totalPages = await fetch(`${env.PUBLIC_BACKEND_URL}/compare/all/${from}`).then(res => res.json()).then(json => json.total_pages)
    const pages = Array.from(Array(totalPages).keys()).map(async page => {
        return await fetchAndTransform(from, page).then(json => callback(json))
    })

    return Promise.all(pages);
}