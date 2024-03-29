<script lang="ts">
  import Header from "../components/Header.svelte";
  import { elections, currentElection, getElections } from "$lib/election";
  import { onMount } from "svelte";
  import "../css/main.css";

  onMount(async () => {
    await getElections()
  })

</script>
<Header/>
<main>
    <slot></slot>
</main>

<style>
  main {
    padding: 0 2rem;
  }
</style>