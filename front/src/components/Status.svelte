<script lang="ts">
  import { get, type Writable } from "svelte/store";

  export let waiting: Promise<any>;
  export let data: Writable<any[]>;
</script>

{#await waiting}
  <div class="status">Chargement... <img src="/pulse.gif" alt=""/> </div>
{:then}
  {#if get(data).length === 0}
    <span class="label">⚠️ Pas de data</span>
  {/if}
{/await}

<style>
  .status {
    display: inline-flex;
    align-items: center;
    background: #00e384;
    color: white;
    border-radius: 20px;
    padding: 0 10px;
  }

  img {
    height: 1.5rem;
    aspect-ratio: 2;
  }
</style>
