<script lang='ts'>
  import { openPopup } from "$lib/dialog";
import Search from "../components/Search.svelte";

</script>
<svelte:head>
  <title>Saison électorale 🌡️</title>
</svelte:head>
<div class="content">
  <span class="high"> Chercher les résultats de <mark> ma commune </mark> </span>
  <Search/>
 <mark class="high"> ou </mark>
  <p><button class="button-blue" on:click={() => openPopup("/graph")}>Voir les résultats par élection pour toute la France</button></p>
  <div class="text">
    <p class="bold">Bienvenue sur Saison électorale, notre comparateur de météo et d'élections. </p>
    <p> À chaque élection, la question de l'impact du beau temps sur l'abstention est un marronier journalistique, soit parce que le soleil pourrait faire préférer aux électeurs d'aller à la plage, soit parce que la pluie pourrait les faire rester chez eux. </p>
    <p> Exemple ci-dessous avec cette vidéo de 2022 du Parisien. </p>
    <p> Notre objectif avec ce comparateur est de <mark> comparer les résultats d'élections et les relevés météorologiques</mark> afin de voir s'il existe une <mark>corrélation. </mark> (Spoiler : non) </p>
    <div class="video" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;"> <iframe style="width:100%;height:100%;position:absolute;left:0px;top:0px;overflow:hidden" frameborder="0" src="https://www.dailymotion.com/embed/video/x89steb?autoplay=0&ui-start-screen-info=true" width="50%" height="50%" allowfullscreen title="Dailymotion Video Player" allow="autoplay"> </iframe> </div>
  </div>
</div>


<style>
  .content {
    height: 100%;
    width: 100%;
    display: flex;
    padding-top: 32px;
    flex-direction: column;
    align-items: center;
    gap: 32px;
  }

  .text {
    margin: 32px 0;
  }

  .video {
    padding: 32px;
    border-radius: 32px;
    overflow: hidden;
    margin: 2rem auto;
  }
</style>
