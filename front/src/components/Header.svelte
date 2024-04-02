<script lang="ts">
  import { openPopup } from "$lib/dialog";
  import Search from "./Search.svelte";
</script>

<header>
  <a class="logo-container" href="/">
    <img class="logo" src="/logo-2.png" alt="Logo" />
    <span class="site-title">
      Saison 🌦️ / électorale 🗳️ </span
    >
  </a>
  <menu>
    <button class="link" on:click={() => openPopup("/map")}>Carte</button>
    <button class="link" on:click={() => openPopup("/graph")}>Graphique</button>
    <a href="/">Par ville</a>
  </menu>
  <div class="search">
    <Search />
  </div>
</header>

<style>
  header {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 0.5rem;
    background: var(--french-white-gradient);
    box-shadow: 0 0 12px 0 rgba(var(--french-blue-rgb), 0.25);
    padding: 1rem;
    margin-bottom: 16px;

    & > * {
      flex: 1;
    }

    & .logo-container {
      all: unset;
      display: flex;
      align-items: center;
      gap: 1rem;
      &:hover {
        cursor: pointer;
      }
    }
  }

  .site-title {
    font-size: 1.5rem;
    font-weight: bold;
    font-family: 'Spectral', serif;
    text-transform: uppercase;
  }

  menu {
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    gap: 32px; 
    
    @media screen and (width < 1200px) {
        justify-content: end;
    }
  }

  .search {
    display: flex;
    justify-content: center;
  }

  .logo {
    transform: rotate(20deg);
    margin-left: 20px;
    height: 5rem;
    transition: all cubic-bezier(0.55, 0.055, 0.675, 0.19) 0.5s;
  }

  .logo-container:hover {
    color: var(--french-red);
    &  .logo {
    transform: rotate(30deg);
    }
  } 
 

</style>
