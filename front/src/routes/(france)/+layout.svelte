<script lang="ts">
    import {elections, currentElection} from "$lib/election";
</script>
<select bind:value={$currentElection}>
    {#each $elections as election}
      <option value={election.value}>
        {election.label}
      </option>
    {/each}
  </select>
<h1>Résultats pour le {$elections.find((e) => $currentElection === e.value)?.label} </h1>
<slot></slot>
