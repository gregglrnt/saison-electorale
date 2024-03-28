<script lang="ts">
    import Map from "../../components/Map.svelte"
    import { writable } from "svelte/store";
    import { onMount } from "svelte";
  
    const elections = writable<any[]>([]);
  
    let currentYear: string;
  
    onMount(async () => {
      await fetch("http://localhost:8000/election/all")
        .then((res) => res.json())
        .then((json) => elections.set(json));
      console.log($elections);
      currentYear = $elections[0].date.split("T")[0];
    });
  </script>
  
  <select bind:value={currentYear}>
    {#each $elections as election}
      <option value={election.date.split("T")[0]}>
        {election.type + " " + election.round + " " + election.date.split("-")[0]}
      </option>
    {/each}
  </select>
  <Map yearSelected={currentYear}></Map>
  