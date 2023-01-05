<script lang="ts">
  import type Filters from "../../interfaces/Filters";
  import MinMaxFilter from "./MinMaxFilter.svelte";

  export let filtersAsCols: boolean = true;

  const filters: Filters = {
    priceMin: null,
    priceMax: null,
  }

  function resetFilters() {
    filters.priceMin = null;
    filters.priceMax = null;
  }

  function applyFilters() {
    console.log(filters);
  }
</script>

<section class="flex flex-col gap-y-3">
  <div class="flex gap-3 flex-wrap" class:flex-col={filtersAsCols}>
    <MinMaxFilter 
      label="Price (CAD):" 
      bind:min={filters.priceMin} 
      bind:max={filters.priceMax} 
    />
    <MinMaxFilter 
      label="Price (CAD):" 
      bind:min={filters.priceMin} 
      bind:max={filters.priceMax} 
    />
  </div>
  <div class="flex flex-row justify-center gap-x-3">
    <button on:click={ resetFilters } class="btn btn-secondary">
      Clear filters
    </button>
    <button on:click={ applyFilters } class="btn btn-primary">
      Search
    </button>
  </div>
</section>
