import {  writable } from "svelte/store";

export const popupLink = writable<string>()

export const openPopup = (link: string) => {
    console.log("link", link);
    popupLink.set(link);
}
