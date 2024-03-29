<script lang="ts">
  import { writable } from "svelte/store";
  import type { SearchValues } from "../models/search";
  import { goto } from "$app/navigation";

    let suggestions : SearchValues[] = [];
    const currentSuggestion = writable<SearchValues>();
    const fetchSuggestions = async(query: string) => {
        console.log("q", query);
        if(query.length <= 3) {
            suggestions = []
            return;
        };
        await fetch(`http://localhost:8000/commune/search?query=${query}`).then(data => data.json()).then(res => suggestions = res)

    }
    
    const searchCity = () => {
        if(!$currentSuggestion) return;
        goto("commune-" + $currentSuggestion.code)
    }

  function selectSuggestion(suggestion: { label: string; code: string; }) {
    currentSuggestion.set(suggestion);
    suggestions = []
  }
</script>

<div class="search-container">
<input list="suggestions" value={$currentSuggestion?.label || ""} type="text" on:input={(e) => fetchSuggestions(e.currentTarget.value)}>
<button on:click={() => searchCity()}>Rechercher ma ville</button>
<datalist id="suggestions">
    {#each suggestions as suggestion}
    <label class="suggestion-label">{suggestion.label}<input name="suggestion" type="radio" value={suggestion.code} on:click={() => selectSuggestion(suggestion)}></label>
{/each}
</datalist>
</div>

<style>
    .search-container {
        position: relative;
    }

    input {
        width: 300px;
    }

    #suggestions {
        display: flex;
        flex-direction: column;
        position: absolute;
        top: 110%;
        width: 300px;
        background: #f9f9f9;
        z-index: 3;
        border-radius: 8px;
        overflow: hidden;

        & input {
            display: none;
        }
    }
    .suggestion-label {
        display: block;
        padding: 0.5px 8px;
        &:hover {
            background: lightblue;
        }
    }
</style>