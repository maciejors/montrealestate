<script lang="ts">
  import { onMount, createEventDispatcher } from "svelte";
  import MinMaxFilter from "./MinMaxFilter.svelte";
  import SelectBoxFilter from "./SelectBoxFilter.svelte";
  import CheckboxFilter from "./CheckboxFilter.svelte";
  import CategorySelectFilter from "./CategorySelectFilter.svelte";
	import { getAllCategories, getAllCities, getAllDistricts, getAllWalkScoresMapped } from "../../database/listings";
	import { FiltersClass, type FiltersType } from "../../types/Filters";
  import copy from "../../utils/copy";

  // defaultFilters contains CURRENTLY APPLIED filters
  export let defaultFilters: FiltersType;

  // filters variable contains VISIBLE FILTERS which MAY NOT HAVE BEEN APPLIED YET
  let filters: FiltersType = new FiltersClass();
  let allCities: string[] = [];
  let allDistricts: string[] = [];
  let allWalkScoresMapped: string[] = [];
  let allCategories: string[] = [];

  $: hideDistrictSelectBox = allDistricts.length === 0;

  const dispatch = createEventDispatcher();

  onMount(async () => {
    filters = copy(defaultFilters);
    allCities = await getAllCities();
    const currCity = filters.city;
    if (currCity !== null) {
      allDistricts = await getAllDistricts(currCity);
    }
    allWalkScoresMapped = await getAllWalkScoresMapped();
    allCategories = await getAllCategories();
    if (filters.categories.length === 0) {
      filters.categories = [...allCategories];
    }
  });

  async function onCityChange() {
    filters.district = '';
    const currCity = filters.city;
    if (currCity !== null) {
      allDistricts = await getAllDistricts(currCity);
    } else {
      allDistricts = [];
    }
  }

  function onResetFilters() {
    filters.city = '';
		filters.district = '';
		filters.categories = [...allCategories];
		filters.minPrice = null;
		filters.maxPrice = null;
		filters.minFloorArea = null;
		filters.maxFloorArea = null;
		filters.minConstructionYear = null;
		filters.maxConstructionYear = null;
		filters.minRooms = null;
		filters.maxRooms = null;
		filters.minBedrooms = null;
		filters.maxBedrooms = null;
		filters.minBathrooms = null;
		filters.maxBathrooms = null;
		filters.minGarages = null;
		filters.maxGarages = null;
		filters.minParkingLots = null;
		filters.maxParkingLots = null;
		filters.onlyNew = false;
		filters.walkScoreMapped = null;
    allDistricts = [];
  }

  function onApplyFilters() {
    dispatch('applyFilters', { filters: filters });
  }
</script>

<section class="flex flex-col gap-y-3">
  <div class="grid gap-y-4 gap-x-20 items-center
    grid-cols-1 xl:grid-cols-2"
  >
    <div class="flex flex-row justify-between gap-x-2">
      <SelectBoxFilter 
        label="City:"
        items={allCities}
        bind:value={filters.city}
        on:valueChanged={onCityChange}
      />
      <SelectBoxFilter 
        label="District:"
        items={allDistricts}
        bind:value={filters.district}
        bind:hidden={hideDistrictSelectBox}
      />
    </div>
    <CategorySelectFilter
      bind:categories={allCategories}
      bind:appliedCategories={filters.categories}
    />
    <MinMaxFilter 
      label="Price (CAD):" 
      bind:min={filters.minPrice} 
      bind:max={filters.maxPrice} 
    />
    <MinMaxFilter 
      label="Floor area (m2):" 
      bind:min={filters.minFloorArea} 
      bind:max={filters.maxFloorArea} 
    />
    <MinMaxFilter 
      label="Constr. Year:" 
      bind:min={filters.minConstructionYear} 
      bind:max={filters.maxConstructionYear} 
    />
    <MinMaxFilter 
      label="Rooms:" 
      bind:min={filters.minRooms} 
      bind:max={filters.maxRooms} 
    />
    <MinMaxFilter 
      label="Bedrooms:" 
      bind:min={filters.minBedrooms} 
      bind:max={filters.maxBedrooms} 
    />
    <MinMaxFilter 
      label="Bathrooms:" 
      bind:min={filters.minBathrooms} 
      bind:max={filters.maxBathrooms} 
    />
    <MinMaxFilter 
      label="Garages:" 
      bind:min={filters.minGarages} 
      bind:max={filters.maxGarages} 
    />
    <MinMaxFilter 
      label="Parking lots:" 
      bind:min={filters.minParkingLots} 
      bind:max={filters.maxParkingLots} 
    />
    <CheckboxFilter
      label="Only new buildings"
      bind:value={filters.onlyNew}
    />
    <SelectBoxFilter 
      label="WalkScore:"
      items={allWalkScoresMapped}
      bind:value={filters.walkScoreMapped}
    />
  </div>
  <div class="flex flex-row justify-center sm:justify-end gap-x-3 mt-4">
    <button on:click={ onResetFilters } class="btn btn-secondary w-28">
      Clear filters
    </button>
    <button on:click={ onApplyFilters } class="btn btn-primary w-28">
      Apply filters
    </button>
  </div>
</section>
