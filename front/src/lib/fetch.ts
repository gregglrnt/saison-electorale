import { generatePathsFromSource, paths, type DataFromAPI } from "./d3"

export const fetchAndTransform = async (url: string, page: number = 0) => {
    const res = await fetch(`http://localhost:8000/compare/all/${url}?page=${page}`)
    const json = await res.json()
    return json as DataFromAPI;
}

export const fetchAllPages = async (from: string) => {
    if(from == undefined) return;
    paths.set([])
    const totalPages = await fetch(`http://localhost:8000/compare/all/${from}`).then(res => res.json()).then(json => json.total_pages)
    const pages = Array.from(Array(totalPages).keys()).map(async page => {
        return await fetchAndTransform(from, page).then(json => generatePathsFromSource(json))
    })

    return Promise.all(pages);
}