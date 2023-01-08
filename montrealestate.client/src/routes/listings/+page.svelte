<svelte:head>
  <title>Search results - montrealestate</title>
</svelte:head>

<script lang="ts">
	import { onDestroy } from "svelte";
  import type { FiltersType } from "../../types/Filters";
  import { filtersStore } from "../../stores/filtersStore";
  import Container from "../../components/Container.svelte";
	import Filters from "../../components/filters/Filters.svelte";

  let filters: FiltersType;
  let filtersVisible = false;

  function showFilters() {
    filtersVisible = true;
  }

  function hideFilters() {
    filtersVisible = false;
  }

  const unsubscribe = filtersStore.subscribe(storedFilters => filters = storedFilters);

  onDestroy(unsubscribe);
</script>

<section class="bg-gray-200 py-4 flex flex-col items-center border-b border-gray-300">
  <div 
    class="flex flex-row justify-between items-center w-full max-w-5xl gap-x-3 px-10"
    class:add-separator={filtersVisible}
  >
    <p class="text-lg">Showing X of Y results:</p>
    {#if filtersVisible}
      <button on:click={hideFilters} class="btn btn-secondary w-28">Hide filters</button>
    {:else}
      <button on:click={showFilters} class="btn btn-secondary w-28">Show filters</button>
    {/if}
  </div>
  <div class="mt-6" class:hidden={!filtersVisible}>
    <Container>
      <Filters />
    </Container>
  </div>
</section>
<Container>
  ehlo
</Container>

<style>
  .add-separator {
    @apply border-b border-gray-400 pb-4;
  }
</style>