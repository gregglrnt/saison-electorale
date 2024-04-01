<script lang="ts">
  import Search from "./Search.svelte";
</script>

<header>
  <a class="logo-container" href="/">
    <img src="/logo.png" alt="Logo"/>
    <span class="site-title"> SAISON/ÉLECTORALE Votre comparateur météo 😎 / élections 🗳️</span>
  </a>


  <Search/>
  <menu>
    <a href="/map">Carte</a>
    <a href="/graph">Graphique</a>
    <a href="/">Par ville</a>
  </menu>
</header>

<style>
  header {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 0.5rem;
    background: #f9f9f9;
    padding: 1rem;

    & .logo-container {
      all: unset;
      flex-basis: 100%;
      display: flex;
      align-items: center;
      /* justify-content: center; */
      gap: 1rem;
      &:hover {
        cursor: pointer;
      }
    }
  }

  .site-title {
    font-size: 1.5rem;
    font-weight: bold;
  }

  menu {
    margin: 0;
    display: flex;
    gap: 1rem;
  }
</style>
