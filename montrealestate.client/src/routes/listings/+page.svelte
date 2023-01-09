<svelte:head>
  <title>Search results - montrealestate</title>
</svelte:head>

<script lang="ts">
	import { onMount } from "svelte";
  import { filtersStore } from "../../stores/filtersStore";
  import Container from "../../components/Container.svelte";
	import Filters from "../../components/filters/Filters.svelte";
	import type { ListingShort } from "../../types/Listings";
	import { getAllCategories, getListings } from "../../database/listings";
	import ListingCard from "../../components/listings/ListingCard.svelte";
	import { goto } from "$app/navigation";
	import type { FiltersType } from "../../types/Filters";
	import copy from "../../utils/copy";

  let listings: ListingShort[] = [];
  let filtersVisible = false;

  function showFilters() {
    filtersVisible = true;
  }

  function hideFilters() {
    filtersVisible = false;
  }

  async function search(filters: FiltersType) {
    hideFilters();
    listings = await getListings(0, 10, filters);
    $filtersStore = copy(filters);
  }

  async function viewListingDetails(listingId: number) {
    goto(`listings/${listingId}`);
  }

  onMount(() => search($filtersStore));
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
      <Filters 
        defaultFilters={$filtersStore}
        on:applyFilters={(e) => search(e.detail.filters)} 
      />
    </Container>
  </div>
</section>
<Container>
  <div class="flex flex-col gap-y-2 py-4">
    {#each listings as listing}
      <ListingCard { listing } on:click={() => viewListingDetails(listing.id)} />
    {/each}
  </div>
</Container>

<style lang="postcss">
  .add-separator {
    @apply border-b border-gray-400 pb-4;
  }
</style>