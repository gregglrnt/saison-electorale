<script lang="ts">
  import { paths } from "$lib/d3";
  import { fetchAllPages } from "$lib/fetch";
  import { writable } from "svelte/store";
  import type { PathType } from "../models/path";

  export let yearSelected: string;
  $: {
    fetchAllPages(yearSelected);
  }
  let hoveredElement = writable<PathType>();
</script>

<div class="container">
  <svg width="900" height="1000">
    {#each $paths as path}
      <path
        id={path.id}
        d={path.d}
        stroke="lightgrey"
        stroke-width="0.5"
        fill={path.fill}
        on:mouseenter={() => hoveredElement.set(path)}
      ></path>
    {/each}
  </svg>
  {#if $hoveredElement}
    <div class="card">
      <p>{$hoveredElement.label}</p>
      <span class={$hoveredElement.weather.split(" ").join("-")} />
      <p>
        {$hoveredElement.abstention
          ? $hoveredElement.abstention + "%"
          : "Pas de résultats"}
      </p>
    </div>
  {/if}
</div>

<style>
  .container {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
  .sun-cloudy::before {
    content: "🌤️";
  }
  .rain::before {
    content: "☔";
  }
  .sun-::before {
    content: "😎";
  }
  .cloudy::before {
    content: "☁️";
  }
  .rain-cloudy::before {
    content: "🌧️";
  }

  path:hover {
    stroke: black;
    cursor: pointer;
  }

  .card {
    border-radius: 20px;
    left: 20px;
    width: 30%;
    padding: 8px;

    & p {
      margin: 0;
    }
  }
</style>
