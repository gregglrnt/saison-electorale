<script lang="ts">
  import { writable } from "svelte/store";
  import type { SearchValues } from "../models/search";
  import { goto } from "$app/navigation";
  import { env } from "$env/dynamic/public";

  let suggestions: SearchValues[] = [];
  const currentSuggestion = writable<SearchValues>();

  const fetchSuggestions = async (query: string) => {
    if (query.length <= 3) {
      suggestions = [];
      return;
    }
    await fetch(`${env.PUBLIC_BACKEND_URL}/commune/search?query=${query}`)
      .then((data) => data.json())
      .then((res) => (suggestions = res));
  };

  const searchCity = () => {
    if (!$currentSuggestion) return;
    goto("commune-" + $currentSuggestion.code);
  };

  function selectSuggestion(suggestion: { label: string; code: string }) {
    currentSuggestion.set(suggestion);
    suggestions = [];
  }

  function handleKeys(ev: KeyboardEvent) {
    console.log("key", ev.key);
    switch (ev.key) {
      case "ArrowDown":
        currentSuggestion.set(
          suggestions[suggestions.indexOf($currentSuggestion) + 1] ||
            suggestions[0]
        );
        break;
      case "ArrowUp":
        currentSuggestion.set(
          suggestions[suggestions.indexOf($currentSuggestion) - 1] ||
            suggestions[0]
        );
    }
  }
</script>

<div class="search-container">
  <input
    placeholder="Entrez ici votre ville, par exemple : Marseille"
    list="suggestions"
    value={$currentSuggestion?.label || ""}
    type="text"
    on:input={(e) => fetchSuggestions(e.currentTarget.value)}
    on:keydown={handleKeys}
  />
  <button on:click={() => searchCity()}>Rechercher ma ville</button>
  <datalist id="suggestions">
    {#each suggestions as suggestion}
      <label class="suggestion-label" class:selected={suggestion === $currentSuggestion}>{suggestion.label}
        <input
          name="suggestion"
          type="radio"
          value={suggestion.code}
          on:click={() => selectSuggestion(suggestion)}
        /></label
      >
    {/each}
  </datalist>
</div>

<style>
  .search-container {
    position: relative;
    display: flex;
    gap: 16px;
  }

  input {
    min-width: 350px;
    background: transparent;
    border: 1px solid darkgray;
    border-radius: 32px;
    padding: 8px 16px;
    color: inherit;
  }

  #suggestions {
    font-family: 'Spectral', sans-serif;
    display: flex;
    flex-direction: column;
    position: absolute;
    top: 110%;
    width: 350px;
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
      background: rgba(50, 157, 255, 0.3);
    }
  }

  .suggestion-label.selected {
    background: rgba(50, 157, 255, 0.2);
  }
</style>
