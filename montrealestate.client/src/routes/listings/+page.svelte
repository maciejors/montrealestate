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
  let filtersHidden = false;

  function showFilters() {
    filtersHidden = false;
  }

  function hideFilters() {
    filtersHidden = true;
  }

  const unsubscribe = filtersStore.subscribe(storedFilters => filters = storedFilters);

  onDestroy(unsubscribe);
</script>

<Container>
  <div class="flex flex-row justify-center gap-x-3 mt-4">
    {#if filtersHidden}
      <button on:click={showFilters} class="btn btn-secondary w-28">Show filters</button>
    {:else}
      <button on:click={hideFilters} class="btn btn-secondary w-28">Hide filters</button>
    {/if}
  </div>
  <Filters bind:hidden={filtersHidden} />
</Container>