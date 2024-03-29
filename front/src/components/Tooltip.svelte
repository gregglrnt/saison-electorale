<script lang="ts">
  import type { Point } from "$lib/scatter";
  import type { PathType } from "../models/path";

  export let content: PathType | Point | null;

  let tooltip: HTMLDivElement;

  const formatTemperature = (content: PathType | Point | null) => {
    const temp = content?.weather?.temperature_celsius?.toFixed(1);
    if(!temp) return "";
    return temp + "°C";
  }

  const setYPosition = (event: MouseEvent) => {
    if(content) {
        tooltip.style.top = event.clientY + "px";
        tooltip.style.left = event.clientX + 60 + "px";
    }
  }

</script>

<svelte:window on:mousemove={setYPosition}></svelte:window>

<div class="card" class:empty={content === null} id="data-card" bind:this={tooltip}>
  <p class="title">{content?.label}</p>
  <span class={content?.weather_status} />
  <p>
    {content?.abstention ? content?.abstention + "% d'abstention" : "Pas de résultats"}
  </p>
  <p>{formatTemperature(content)}</p>
</div>

<style>

.card {
    border-radius: 20px;
    left: 20px;
    width: 30%;
    padding: 16px;
    position: fixed;
    left: 80%;
    background: #F9F9F9;
  }

  .title {
    font-weight: bold;
  }

.empty {
    display: none;
} 
  .sun.cloudy::before {
    content: "🌤️";
  }
  .rain::before {
    content: "☔";
  }
  .sun::before {
    content: "😎";
  }
  .cloudy::before {
    content: "☁️";
  }
  .rain.cloudy::before {
    content: "🌧️";
  }
</style>
