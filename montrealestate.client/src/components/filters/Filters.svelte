<script lang="ts">
  import { onMount, createEventDispatcher } from "svelte";
  import { filtersStore } from "../../stores/filtersStore";
  import MinMaxFilter from "./MinMaxFilter.svelte";
  import SelectBoxFilter from "./SelectBoxFilter.svelte";
  import CheckboxFilter from "./CheckboxFilter.svelte";
  import CategorySelectFilter from "./CategorySelectFilter.svelte";
	import { getAllCategories, getAllCities, getAllDistricts, getAllWalkScoresMapped } from "../../database/listings";

  export let hidden: boolean = false;

  const dispatch = createEventDispatcher();

  let allCities: string[] = [];
  let allDistricts: string[] = [];
  let allWalkScoresMapped: string[] = [];
  let allCategories: string[] = [];

  $: hideDistrictSelectBox = allDistricts.length === 0;

  onMount(async () => {
    allCities = await getAllCities();
    const currCity = $filtersStore.city;
    if (currCity !== null) {
      allDistricts = await getAllDistricts(currCity);
    }
    allWalkScoresMapped = await getAllWalkScoresMapped();
    allCategories = await getAllCategories();
    $filtersStore.categories = allCategories;
  });

  async function onCityChange() {
    $filtersStore.district = '';
    const currCity = $filtersStore.city;
    if (currCity !== null) {
      allDistricts = await getAllDistricts(currCity);
    } else {
      allDistricts = [];
    }
  }

  function hideFilters() {
    hidden = true;
  }

  function onResetFilters() {
    $filtersStore.city = '';
		$filtersStore.district = '';
		$filtersStore.categories = allCategories;
		$filtersStore.minPrice = null;
		$filtersStore.maxPrice = null;
		$filtersStore.minFloorArea = null;
		$filtersStore.maxFloorArea = null;
		$filtersStore.minConstructionYear = null;
		$filtersStore.maxConstructionYear = null;
		$filtersStore.minRooms = null;
		$filtersStore.maxRooms = null;
		$filtersStore.minBedrooms = null;
		$filtersStore.maxBedrooms = null;
		$filtersStore.minBathrooms = null;
		$filtersStore.maxBathrooms = null;
		$filtersStore.minGarages = null;
		$filtersStore.maxGarages = null;
		$filtersStore.minParkingLots = null;
		$filtersStore.maxParkingLots = null;
		$filtersStore.onlyNew = false;
		$filtersStore.walkScoreMapped = null;
    allDistricts = [];
  }

  function onApplyFilters() {
    dispatch('applyFilters');
  }
</script>

<section class="flex flex-col gap-y-3" class:hidden={hidden}>
  <div class="grid gap-y-4 gap-x-20 items-center
    grid-cols-1 xl:grid-cols-2"
  >
    <div class="flex flex-row justify-between gap-x-2">
      <SelectBoxFilter 
        label="City:"
        items={allCities}
        bind:value={$filtersStore.city}
        on:valueChanged={onCityChange}
      />
      <SelectBoxFilter 
        label="District:"
        items={allDistricts}
        bind:value={$filtersStore.district}
        bind:hidden={hideDistrictSelectBox}
      />
    </div>
    <CategorySelectFilter
      bind:items={allCategories}
      bind:selectedItems={$filtersStore.categories}
    />
    <MinMaxFilter 
      label="Price (CAD):" 
      bind:min={$filtersStore.minPrice} 
      bind:max={$filtersStore.maxPrice} 
    />
    <MinMaxFilter 
      label="Floor area (m2):" 
      bind:min={$filtersStore.minFloorArea} 
      bind:max={$filtersStore.maxFloorArea} 
    />
    <MinMaxFilter 
      label="Constr. Year:" 
      bind:min={$filtersStore.minConstructionYear} 
      bind:max={$filtersStore.maxConstructionYear} 
    />
    <MinMaxFilter 
      label="Rooms:" 
      bind:min={$filtersStore.minRooms} 
      bind:max={$filtersStore.maxRooms} 
    />
    <MinMaxFilter 
      label="Bedrooms:" 
      bind:min={$filtersStore.minBedrooms} 
      bind:max={$filtersStore.maxBedrooms} 
    />
    <MinMaxFilter 
      label="Bathrooms:" 
      bind:min={$filtersStore.minBathrooms} 
      bind:max={$filtersStore.maxBathrooms} 
    />
    <MinMaxFilter 
      label="Garages:" 
      bind:min={$filtersStore.minGarages} 
      bind:max={$filtersStore.maxGarages} 
    />
    <MinMaxFilter 
      label="Parking lots:" 
      bind:min={$filtersStore.minParkingLots} 
      bind:max={$filtersStore.maxParkingLots} 
    />
    <CheckboxFilter
      label="Only new buildings"
      bind:value={$filtersStore.onlyNew}
    />
    <SelectBoxFilter 
      label="WalkScore:"
      items={allWalkScoresMapped}
      bind:value={$filtersStore.walkScoreMapped}
    />
  </div>
  <div class="flex flex-row justify-center gap-x-3 mt-4" class:hidden={hidden}>
    <button on:click={ hideFilters } class="btn btn-secondary w-28">
      Hide filters
    </button>
    <button on:click={ onResetFilters } class="btn btn-secondary w-28">
      Clear filters
    </button>
    <button on:click={ onApplyFilters } class="btn btn-primary w-28">
      Apply filters
    </button>
  </div>
</section>
