<script lang="ts">
  import Header from "../components/Header.svelte";
  import { getElections } from "$lib/election";
  import { onMount } from "svelte";
  import "../css/fonts/font-face.css"
  import "../css/main.css";
  import Dialog from "../components/Dialog.svelte";
  import Footer from "../components/Footer.svelte";

  onMount(async () => {
    await getElections()
  })

</script>
<div class="body">
  <Header/>
  <main>
      <slot></slot>
      <Dialog/>
  </main>
  <Footer/>  
</div>

<style>
  .body {
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
  }

</style>