<script lang="ts">
  import { getDepartmentName } from "$lib/utils";
  import { getGlobalClimate, medianTemperature } from "$lib/weather";
  import SpecificScatter from "../../components/SpecificScatter.svelte";
  import type { PageData } from "./$types";

  export let data: PageData;
  $: abstentions = data.electionWeather.map(
    (election) => election.results.abstention
  );
  $: average = abstentions.reduce((a, b) => a + b, 0) / abstentions.length;
  $: orderedByAbstention = data.electionWeather.sort(
    (e1, e2) => e1.results.abstention - e2.results.abstention
  );
  $: biggest = orderedByAbstention[0];
  $: lowest = orderedByAbstention[orderedByAbstention.length - 1];
</script>

<div class="title">
  <h1>
    <u> {data.commune.label} </u> - {getDepartmentName(
      data.commune.departement
    )} ({data.commune.zip})
  </h1>
</div>
{#if abstentions.length < 1}
  <span> ⚠️ Pas de données </span>
{/if}
<span></span>
{#if biggest && lowest}
  <p><b>Moyenne abstention : </b> {average.toFixed(1)} %</p>
  <p>
    <b> Plus basse abstention : </b>
    {biggest.election.label} - 🗳️{biggest.results.abstention}% - 🌡️{medianTemperature(
      biggest.weather
    )}°C en moyenne - {getGlobalClimate(biggest.weather)}
  </p>
  <p>
    <b> Plus forte abstention : </b>
    {lowest.election.label} - 🗳️{lowest.results.abstention}% - 🌡️{medianTemperature(
      lowest.weather
    )}°C en moyenne - {getGlobalClimate(lowest.weather)}
  </p>
{/if}
<SpecificScatter props={data} />

<style>
  .title {
    display: flex;
    gap: 2rem;
    align-items: center;
  }

  h1 {
    margin: 0;
    color: #ff473e;
  }

  h1 u {
    text-decoration-style: dashed;
  }
</style>
