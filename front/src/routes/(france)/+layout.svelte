<script lang="ts">
  import { page } from "$app/stores";
  import { elections, currentElection, getElections } from "$lib/election";
  import Select from "../../components/Select.svelte";
</script>

<div class="content">
  <div class="toggle">
    <Select />
    <a
      class="button button-blue"
      href={$page.url.pathname === "/map" ? "/graph" : "/map"}
    >
      Voir sous forme de {$page.url.pathname === "/map"
        ? "graphe 📈"
        : "carte 🗺️"}
    </a>
  </div>
  <h1>
    Résultats pour le <mark
      >{$elections.find((e) => $currentElection === e.value)?.label}</mark
    >
  </h1>
  <slot />
</div>

<style>
  .toggle {
    display: flex;
    gap: 32px;
  }
</style>
