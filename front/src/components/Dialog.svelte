<script lang="ts">
  import { navigating } from "$app/stores";
  import { popupLink } from "$lib/dialog";
  import { fly } from "svelte/transition";
  import Select from "./Select.svelte";

  let popup: HTMLDialogElement;

  $: if ($navigating) {
    close()
  }
  $: if ($popupLink) popup.showModal();

  const close = () => {
    popupLink.set("");
    popup.close();
  }

</script>

<dialog bind:this={popup} transition:fly>
  <button class="dialog-x" on:click={() => close()}
    ><svg
      xmlns="http://www.w3.org/2000/svg"
      width="2rem"
      height="2rem"
      viewBox="0 0 21 21"
      ><path
        fill="none"
        stroke="currentColor"
        stroke-linecap="round"
        stroke-linejoin="round"
        d="m7.5 7.5l6 6m0-6l-6 6"
      /></svg
    ></button
  >
  <div class="dialog-content">
    <p class="high center">Choisir une élection</p>
    <Select />
    <a class="button" href={$popupLink}>Allons-y!</a>
  </div>
</dialog>

<style>
  dialog {
    z-index: 10;
    border-radius: 32px;
    border: none;
    box-shadow: 0 0 4px 0 rgba(0, 0, 0, 0.25);
    padding: 32px;
    overflow: hidden;
    min-height: 30%;
    min-width: 30%;
    color: inherit;
  }

  dialog::backdrop {
    background: rgba(0, 0, 0, 0.25);
  }

  .dialog-content {
    display: flex;
    flex-direction: column;
    gap: 32px;
    height: 100%;
    justify-content: center;
    max-width: 300px;
    margin: auto;
    margin-top: 32px;
  }

  .dialog-x {
    all: unset;
    position: absolute;
    top: 16px;
    right: 16px;
    border-radius: 50%;
    width: 20px;
    height: 20px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    color: white;
    background: var(--french-red);
    padding: 4px;

    &:hover {
        cursor: pointer;
    }
  }
</style>
