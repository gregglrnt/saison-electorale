<script lang="ts">
  import { generatePathsFromSource, paths } from "$lib/map";
  import { fetchAllPagesAnd } from "$lib/fetch";
  import { writable } from "svelte/store";
  import type { PathType } from "../models/path";
  import { currentElection } from "$lib/election";
  import Tooltip from "./Tooltip.svelte";
  let status = "";
  $: {
    status = "loading"
    fetchAllPagesAnd($currentElection, generatePathsFromSource).then(() => status = "")
  }
  let hoveredElement = writable<PathType | null>(null);
</script>

<span class="status" class:loading={status === "loading"}> {status} </span>
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
        on:mouseleave={() => hoveredElement.set(null)}
        aria-describedby="data-card"
        role="figure"
      ></path>
    {/each}
  </svg>
  <Tooltip content={$hoveredElement}/>
</div>

<style>
  .container {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
 

  path:hover {
    stroke: black;
    cursor: pointer;
  }
</style>
