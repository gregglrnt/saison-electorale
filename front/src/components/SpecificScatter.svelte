<script lang="ts">
  import {
    line,
    scaleLinear,
    scaleTime,
    type NumberValue,
    scaleDiverging,
    interpolateSpectral,
    interpolateGreys,
    interpolatePuBu,
    scaleOrdinal,
    scaleBand,
    interpolateReds,
  } from "d3";
  import type { CommuneWithResult, ResultWeather } from "../models/results";
  import { onMount } from "svelte";
  import { writable } from "svelte/store";
  import { type Election } from "$lib/election";
  import Card from "./Card.svelte";

  export let props: CommuneWithResult;
  const hoveredElection = writable<ResultWeather | null>();
  
  $: data = props.electionWeather.sort(
    (x, y) => +y.election.date - +x.election.date
  );

  let svg: SVGSVGElement;
  let width = 700;
  let height = 500;

  const padding = { top: 20, right: 40, bottom: 40, left: 40 };

  $: dates = data.map((election) =>
    election.election.date.toLocaleDateString()
  ).reverse();

  const yTicks = [-10, 0, 10, 20, 30, 40];

  $: xScale = scaleBand()
    .domain(dates)
    .range([padding.left, width - padding.right]);

  $: tempScale = scaleLinear()
    .domain([-10, 40])
    .range([height - padding.bottom, padding.top]);

  const rainScale = scaleLinear()
    .domain([0, 6])
    .range([height - padding.bottom, padding.top]);

  $: abstentionScale = scaleLinear()
    .domain([0, 100])
    .range([height - padding.bottom, padding.top]);

  const colorScale = scaleDiverging(interpolateReds).domain([0, 100]);

  onMount(resize);
  function resize() {
    ({ width, height } = svg.getBoundingClientRect());
  }

  // const lineBuilder = line<Date | NumberValue>().x((d) => xScale(d)).y((d) => abstentionScale(d))
  $: path = `M${data.map((el) => `${xScale(el.election.date.toLocaleDateString())},${abstentionScale(el.results.abstention)}`).join("L")}`;
</script>

<svelte:window on:resize={() => resize()} />
<div role="figure" class="graph" on:mouseleave={() => hoveredElection.set(null)}>
  <svg {width} {height} bind:this={svg}>
    <g class="axis y-axis">
      {#each yTicks as tick}
        <g class="tick tick-{tick}" transform="translate(0, {tempScale(tick)})">
          <line x1={padding.left} x2={xScale(dates[dates.length - 1])} />
          <text x={padding.left - 8} y="+4">{tick + "°C"}</text>
        </g>
      {/each}
    </g>

    <g class="axis x-axis">
      {#each dates as date}
        <g class="tick" transform="translate({xScale(date)},0)">
          <line y1={tempScale(-10)} y2={tempScale(40)} />
          <!-- <text y={height - padding.bottom + 16}> {date} </text> -->
        </g>
      {/each}
    </g>

    {#each data as { election, weather, results }}
      {#each weather as meteo}
        {#if meteo.temperature_celsius}
          <circle
            class="temperature"
            cy={tempScale(meteo.temperature_celsius)}
            cx={xScale(election.date.toLocaleDateString())}
            r="4"
          />
        {/if}
      {/each}
      <circle
        class="abstention"
        r="5"
        role="figure"
        fill={colorScale(results.abstention)}
        cy={abstentionScale(results.abstention)}
        cx={xScale(election.date.toLocaleDateString())}
        on:mouseenter={() =>
          hoveredElection.set({
            election: election,
            results: results,
            weather: weather,
          })}
      />
    {/each}

    <path class="path-line" d={path} />
  </svg>
  {#if $hoveredElection}
    <Card content={$hoveredElection} />
  {/if}
</div>

<style>
  .graph {
    display: grid;
    grid-template-columns: 1fr 200px;

    @media screen and (width < 600px) {
      grid-template-columns: 1fr;
    }
  }
  svg {
    width: 100%;
    height: 100%;
  }
  .temperature {
    fill: orange;
    opacity: 0.2;
  }

  .abstention {
    &:hover {
      cursor: pointer;
      stroke: purple;
    }
  }

  text {
    font-size: 12px;
    fill: #999;
  }

  .x-axis text {
    text-anchor: start;
  }

  .y-axis text {
    text-anchor: end;
  }

  .tick line {
    stroke: #ddd;
    stroke-dasharray: 2;
  }

  path {
    stroke: #ff473e;
    fill: none;
  }
</style>
