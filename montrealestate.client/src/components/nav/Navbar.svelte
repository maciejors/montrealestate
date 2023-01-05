<script lang="ts">
  import type NavbarTileItem from "../../interfaces/NavbarTileItem";
  import NavbarTile from "./NavbarTile.svelte";

  export let items: NavbarTileItem[];
</script>

<nav 
  class="sticky top-0 w-full 
    py-2 px-2
    sm:py-5 sm:px-10
    bg-white
    border-b border-gray-300"
>
  <div class="flex flex-col sm:flex-row items-center">
    <div class="inline-block 
      mb-1 pb-1 px-4 border-gray-200 border-b
      sm:mb-0 sm:pr-8 sm:border-b-0 sm:border-r"
    >
      <h2 class="title">montrealestate</h2>
    </div>
    <div class="flex sm:ml-4">
      {#each items as item (item.id)}
        <NavbarTile 
          label={ item.label }
          href={ item.href }
        />
      {/each}
    </div>
  </div>
</nav>

<style>
  .title {
    @apply text-2xl font-bold text-primary;
    font-family: Georgia, 'Times New Roman', Times, serif
  }
</style>