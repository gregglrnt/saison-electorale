<script lang="ts">
  import { onMount } from "svelte";
  import { scaleLinear } from "d3-scale";
  import { definePointsDefault, points, type Point } from "$lib/scatter";
  import { fetchAllPagesAnd } from "$lib/fetch";
  import { writable } from "svelte/store";
  import { currentElection } from "$lib/election";
  import Tooltip from "./Tooltip.svelte";
  import Status from "./Status.svelte";
  let svg: SVGSVGElement;
  let width = 700;
  let height = 500;

  const padding = { top: 20, right: 40, bottom: 40, left: 40 };
  const hoverPoint = writable<Point | null>(null);
  const rainTicks = [0, 1, 2, 3, 4, 5, 6];
  const temperatureTicks = [-10, 0, 10, 20, 30, 40];

  const comparaison = writable<"rain" | "temperature">("rain");

  $: domain =
    $comparaison === "rain"
      ? [rainTicks[0], rainTicks[rainTicks.length - 1]]
      : [temperatureTicks[0], temperatureTicks[temperatureTicks.length - 1]];

  $: fetch = fetchAllPagesAnd($currentElection, definePointsDefault);

  $: xScale = scaleLinear()
    .domain(domain)
    .range([padding.left, width - padding.right]);

  $: yScale = scaleLinear()
    .domain([0, 100])
    .range([height - padding.bottom, padding.top]);

  $: xTicks = $comparaison === "rain" ? rainTicks : temperatureTicks;

  $: yTicks = [0, 20, 40, 60, 80, 100];

  onMount(resize);

  function resize() {
    ({ width, height } = svg.getBoundingClientRect());
  }

  function toggleComparaison() {
    $comparaison === "rain"
      ? comparaison.set("temperature")
      : comparaison.set("rain");
  }
</script>

<Status waiting={fetch} data={points}/>

<div class={`graph ${$comparaison}`}>
  <svg bind:this={svg} {width} {height}>
    <!-- y axis -->
    <g class="axis y-axis">
      {#each yTicks as tick}
        <g class="tick tick-{tick}" transform="translate(0, {yScale(tick)})">
          <line x1={padding.left} x2={xScale(domain[domain.length - 1])} />
          <text x={padding.left - 8} y="+4">{tick + "%"}</text>
        </g>
      {/each}
    </g>

    <!-- x axis -->
    <g class="axis x-axis">
      {#each xTicks as tick}
        <g class="tick" transform="translate({xScale(tick)},0)">
          <line y1={yScale(0)} y2={yScale(100)} />
          <text y={height - padding.bottom + 16}>{tick + ($comparaison === "rain" ? "mm" : "°C")}</text>
        </g>
      {/each}
    </g>

    <!-- data -->
    {#each $points as point}
      <circle
        role="figure"
        aria-describedby="data-card"
        cx={xScale($comparaison === "rain" ? point.rain : point.temperature)}
        cy={yScale(point.abstention)}
        r="5"
        on:mouseenter={() => hoverPoint.set(point)}
        on:mouseleave={() => hoverPoint.set(null)}
      />
    {/each}
  </svg>

  <div class="toggle-bar">
    <button on:click={() => toggleComparaison()}>
      Comparer avec la {$comparaison === "rain" ? "température 🌡️" : "pluie ☔"}
    </button>
  </div>
</div>

<Tooltip content={$hoverPoint} />

<style>
  .graph {
    display: flex;
    flex-direction: column;
  }

  svg {
    width: 50%;
    height: 50%;
  }

  circle {
    fill: lightskyblue;
    fill-opacity: 0.4;

    &:hover {
      stroke: black;
    }
  }

  .temperature circle {
    fill: lightsalmon;
  }

  .tick line {
    stroke: #ddd;
    stroke-dasharray: 2;
  }

  text {
    font-size: 12px;
    fill: #999;
  }

  .x-axis text {
    text-anchor: middle;
  }

  .y-axis text {
    text-anchor: end;
  }

  .toggle-bar {
    display: flex;
    justify-content: center;
  }

</style>
