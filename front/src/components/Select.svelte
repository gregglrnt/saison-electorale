<script lang="ts">
  import { elections, currentElection } from "$lib/election";
</script>

<select bind:value={$currentElection}>
  {#each $elections as election}
    <option value={election.value}>
      {election.label}
    </option>
  {/each}
</select>

<style>
  select {
    padding: 8px;
    border-radius: 8px;
    background: transparent;
    color: inherit;
    border-color: var(--french-blue);
    font-family: inherit;
  }

  option {
    background: var(--french-white);
  }
</style>
