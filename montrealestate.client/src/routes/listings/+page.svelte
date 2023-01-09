<svelte:head>
  <title>Search results - montrealestate</title>
</svelte:head>

<script lang="ts">
	import { onMount } from "svelte";
  import { filtersStore } from "../../stores/filtersStore";
  import Container from "../../components/Container.svelte";
	import Filters from "../../components/filters/Filters.svelte";
	import type { ListingShort } from "../../types/Listings";
	import { getListings } from "../../database/listings";
	import ListingCard from "../../components/listings/ListingCard.svelte";
	import { goto } from "$app/navigation";
	import type { FiltersType } from "../../types/Filters";
	import copy from "../../utils/copy";
	import PageNavigation from "../../components/PageNavigation.svelte";
	import SpinnerLoader from "../../components/SpinnerLoader.svelte";

  let listings: ListingShort[] = [];
  let filtersVisible = false;
  // pagination variables:
  let startFrom = 0;
  let count = 10
  let totalCount = 22;
  $: displayedCount = listings.length;

  function showFilters() {
    filtersVisible = true;
  }

  function hideFilters() {
    filtersVisible = false;
  }

  async function search(filters: FiltersType) {
    listings = [];
    setTimeout(async () => {
      listings = await getListings(startFrom, count, filters);
    }, 1000);
  }

  async function onFiltersChanged(newFilters: FiltersType) {
    hideFilters();
    startFrom = 0;
    search(newFilters);
    $filtersStore = copy(newFilters);
  }

  async function onPageChanged() {
    await search($filtersStore);
  }

  async function viewListingDetails(listingId: number) {
    goto(`listings/${listingId}`);
  }

  onMount(() => search($filtersStore));
</script>

<section class="bg-gray-200 py-4 flex flex-col items-center border-b border-gray-300">
  <div 
    class="flex flex-row justify-end items-center w-full max-w-5xl gap-x-3 px-10"
    class:add-separator={filtersVisible}
  >
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
        on:applyFilters={(e) => onFiltersChanged(e.detail.filters)} 
      />
    </Container>
  </div>
</section>
<Container>
  <div class="flex flex-col items-center w-full mt-2 gap-y-1
      md:flex-row md:justify-start">
    <PageNavigation 
      bind:startFrom={startFrom} 
      count={count} 
      totalCount={totalCount}
      on:pageChanged={onPageChanged}
    />
    <p class="text-sm text-gray-700 pt-1 px-8 border-gray-300 border-t
      md:pt-0 md:pr-0 md:pl-6 md:ml-6 md:border-t-0 md:border-l"
    >Showing {displayedCount} of {totalCount} results:</p>
  </div>
  <div class="pb-8 pt-12" class:hidden={listings.length > 0}>
    <SpinnerLoader />
  </div>
  <div class="flex flex-col gap-y-2 py-4">
    {#each listings as listing}
      <ListingCard { listing } on:click={() => viewListingDetails(listing.id)} />
    {/each}
  </div>
  <div class="mb-4">
    <PageNavigation 
      bind:startFrom={startFrom} 
      count={count} 
      totalCount={totalCount}
      on:pageChanged={onPageChanged}
    />
  </div>
</Container>

<style lang="postcss">
  .add-separator {
    @apply border-b border-gray-400 pb-4;
  }
</style>