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
  <p><mark>Moyenne abstention : </mark> {average.toFixed(1)} %</p>
  <p>
    <mark> Plus basse abstention : </mark>
    {biggest.election.label} - 🗳️<b>{biggest.results.abstention}% d'abstention</b> - 🌡️{medianTemperature(
      biggest.weather
    )}°C en moyenne - {getGlobalClimate(biggest.weather)}
  </p>
  <p>
    <mark> Plus forte abstention : </mark>
    {lowest.election.label} - <b>🗳️{lowest.results.abstention}% d'abstention </b> - 🌡️{medianTemperature(
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
    margin-bottom: 16px;
    color: var(--french-red);
  }

  h1 u {
    text-decoration-style: dashed;
  }
</style>
