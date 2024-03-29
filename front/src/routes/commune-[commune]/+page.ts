import type { CommuneWithResult } from "../../models/results";
import type { PageLoad } from "./$types"

export const load : PageLoad = async ({fetch, params}) => {
    console.log(params.commune)
    const data : CommuneWithResult = await fetch(`http://localhost:8000/commune/${params.commune}/results`).then(res => res.json()).catch(() => console.error("error"));
    return {
        results: data,
    }
}