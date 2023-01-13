<svelte:head>
  <title>Home - montrealestate</title>
</svelte:head>

<script lang="ts">
  import { goto } from "$app/navigation";
  import { onMount } from "svelte";
  import { filtersStore } from "../stores/filtersStore";
  import Container from "../components/Container.svelte";
  import SelectBoxFilter from "../components/filters/SelectBoxFilter.svelte";
  import { getAllCities } from "../database/listings";
	import { FiltersClass } from "../types/Filters";

  let allCities: string[] = [];
  let selectedCity: string = '';

  onMount(async () => {
    allCities = await getAllCities();
  });
  
  function onCitySelect() {
    filtersStore.update(filters => {
      filters = new FiltersClass();
      filters.city = selectedCity;
      return filters;
    }); 
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