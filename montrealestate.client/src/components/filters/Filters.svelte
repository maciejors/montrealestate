<script lang="ts">
  import { onMount, createEventDispatcher } from "svelte";
  import { filtersStore } from "../../stores/filtersStore";
  import type Filters from "../../interfaces/Filters";
  import MinMaxFilter from "./MinMaxFilter.svelte";
  import SelectBoxFilter from "./SelectBoxFilter.svelte";

  const dispatch = createEventDispatcher();

  let allCities: string[] = [];
  let allDistricts: string[] = [];
  let allWalkScoresMapped: string[] = [];
  let allCategories: string[] = [];

  onMount(async () => {
    allCities = ['montreal', 'warsaw'];
    allDistricts = ['west', 'east'];
    allWalkScoresMapped = ['walkscore1', 'walkscore2'];
    allCategories = ['semi-detached', 'ruins'];
  });

  function resetFilters() {
    for (const filterName of Object.keys($filtersStore)) {
      $filtersStore[filterName as keyof Filters] = null; 
    }
  }

  function applyFilters() {
    dispatch('applyFilters');
  }
</script>

<section class="flex flex-col gap-y-3">
  <div class="grid">
    <MinMaxFilter 
      label="Price (CAD):" 
      bind:min={$filtersStore.minPrice} 
      bind:max={$filtersStore.maxPrice} 
    />
  </div>
  <div class="flex flex-row justify-center gap-x-3">
    <button on:click={ resetFilters } class="btn btn-secondary">
      Clear filters
    </button>
    <button on:click={ applyFilters } class="btn btn-primary">
      Apply filters
    </button>
  </div>
</section>
