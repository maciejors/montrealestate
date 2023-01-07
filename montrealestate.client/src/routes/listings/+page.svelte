<svelte:head>
  <title>Search results - montrealestate</title>
</svelte:head>

<script lang="ts">
  import { error } from "@sveltejs/kit";
	import { onDestroy } from "svelte";
  import type Filters from "../../interfaces/Filters";
  import { filtersStore } from "../../stores/filtersStore";

  let filters: Filters;

  const unsubscribe = filtersStore.subscribe(storedFilters => filters = storedFilters);

  onDestroy(unsubscribe);
</script>
<h1 class="text-3xl">city: { filters.city }</h1>