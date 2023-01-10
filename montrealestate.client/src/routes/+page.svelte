<svelte:head>
  <title>Home - montrealestate</title>
</svelte:head>

<script lang="ts">
  import { goto } from "$app/navigation";
  import { onMount } from "svelte";
  import { filtersStore } from "../stores/filtersStore";
  import Container from "../components/Container.svelte";
  import SelectBoxFilter from "../components/filters/SelectBoxFilter.svelte";
  import { getAllCategories, getAllCities } from "../database/listings";
	import { FiltersClass } from "../types/Filters";

  let allCities: string[] = [];
  let allCategories: string[] = [];
  let selectedCity: string = '';

  onMount(async () => {
    allCities = await getAllCities();
    allCategories = await getAllCategories();
  });
  
  function onCitySelect() {
    filtersStore.update(filters => {
      filters = new FiltersClass();
      filters.city = selectedCity;
      return filters;
    }); 
  }

  function onCategorySelect(category: string) {
    filtersStore.update(filters => {
      filters = new FiltersClass();
      filters.categories = [ category ];
      return filters;
    });
    search();
  }

  function search() {
    goto('/listings');
  }
</script>

<section class="bg-home bg-auto py-10">
  <Container>
    <h1 class="text-3xl text-white font-bold mb-2 text-center">Montreal is Real</h1>
    <h3 class="text-xl text-white mb-8 text-center">No. 1 property website for Montreal and surrounding areas</h3>
    <div class="card p-4 flex flex-row gap-x-2 items-center">
      <SelectBoxFilter label="Explore by city:" items={allCities} bind:value={selectedCity} on:valueChanged={onCitySelect} />
      <button 
        class="btn btn-primary h-8" 
        disabled={selectedCity === ''}
        on:click={search}
      >
        Search
    </button>
    </div>
  </Container>
</section>
<section class="pb-10 pt-4">
  <Container>
    <h3 class="text-lg w-full mb-4">Browse by category:</h3>
    <div class="flex flex-row flex-wrap w-full gap-x-4 gap-y-2">
      {#each allCategories as category}
        <button class="btn btn-secondary" on:click={() => onCategorySelect(category)}>
          { category }
        </button>
      {/each}
    </div>
  </Container>
</section>