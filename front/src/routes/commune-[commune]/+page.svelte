<script lang="ts">
  import type { PageData } from "./$types";

    export let data: PageData;
    console.log(data);
</script>

<h1>Bienvenue à {data.results.label} </h1>
<p> {data.results.departement} ({data.results.zip})</p>

{#each data.results.Results as res}
<p>{res.ballot.date} - {res.abstention}</p>
{/each}