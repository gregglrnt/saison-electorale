<script lang="ts">
  import type { Election } from "$lib/election";
  import { getGlobalClimate, medianTemperature } from "$lib/weather";
  import type { Result, ResultWeather } from "../models/results";

    export let content : ResultWeather;

</script>


<div class="card">
    <h3> 🗳️ {content.election.label} <span> {getGlobalClimate(content.weather) || ""} </span> </h3>
    <small> {content.election.date.toLocaleDateString('fr-FR')} </small>
    <p> 🌡️ {medianTemperature(content.weather)} °C en moyenne </p>
    <p> 👤 Abstention : {content.results.abstention}% </p>
</div>

<style>
    .card {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
</style>