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
  let hideFilters = false;

  const unsubscribe = filtersStore.subscribe(storedFilters => filters = storedFilters);

  onDestroy(unsubscribe);
</script>

<Container>
  <div class="flex flex-row justify-center gap-x-3 mt-4">
    <button on:click={() => hideFilters = false} class="btn btn-secondary w-28">
      Show filters
    </button>
  </div>
  <Filters bind:hidden={hideFilters} />
</Container>