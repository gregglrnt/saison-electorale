import { env } from "$env/dynamic/public";
import type { CommuneWithResult } from "../../models/results";
import type { PageLoad } from "./$types"

export const load : PageLoad = async ({fetch, params}) => {
    const data : CommuneWithResult = await fetch(`${env.PUBLIC_BACKEND_URL}/commune/${params.commune}/results`).then(res => res.json()).catch(() => console.error("error"));
    return {
        results: data,
    }
}