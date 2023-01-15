<script lang="ts">
  import { onMount, createEventDispatcher } from "svelte";
  import MinMaxFilter from "./MinMaxFilter.svelte";
  import SelectBoxFilter from "./SelectBoxFilter.svelte";
  import CheckboxFilter from "./CheckboxFilter.svelte";
	import { getAllCities, getAllDistricts } from "../../database/listings";
	import { FiltersClass, type FiltersType } from "../../types/Filters";
  import copy from "../../utils/copy";

  // defaultFilters contains CURRENTLY APPLIED filters
  export let defaultFilters: FiltersType;

  // filters variable contains VISIBLE FILTERS which MAY NOT HAVE BEEN APPLIED YET
  let filters: FiltersType = new FiltersClass();
  let allCities: string[] = [];
  let allDistricts: string[] = [];
  let allWalkScoresDesc = ['Car-dependent', 'Somewhat walkable', 'Very walkable', "Walker's paradise"];
  let allWalkScoreThresholds = [0, 50, 70, 90];

  $: hideDistrictSelectBox = allDistricts.length === 0;

  let displayError = false;
  const minmaxValuesValid = {
    price: true,
    floorArea: true,
    constructionYear: true,
    noRooms: true,
    noBedrooms: true,
    noBathrooms: true,
    noGarages: true,
    noParkingLots: true,
  };

  const dispatch = createEventDispatcher();

  onMount(async () => {
    filters = copy(defaultFilters);
    allCities = await getAllCities();
    const currCity = filters.city;
    if (currCity !== null) {
      allDistricts = await getAllDistricts(currCity);
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
    displayError = false;
    filters.city = '';
		filters.district = '';
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
		filters.walkScoreThreshold = null;
    allDistricts = [];
  }

  function onApplyFilters() {
    let formValid = true;
    for (let isFieldValid of Object.values(minmaxValuesValid)) {
      if (!isFieldValid) {
        formValid = false;
        break;
      }
    }
    if (formValid === false) {  // form invalid
      displayError = true;
      return;
    }  
    displayError = false;
    dispatch('applyFilters', { filters: filters });
  }
</script>

<section class="flex flex-col gap-y-3">
  <div class="grid gap-y-4 gap-x-20 items-center
    grid-cols-1 xl:grid-cols-2"
  >
    <div class:xl:col-span-2={hideDistrictSelectBox}>
      <SelectBoxFilter 
        label="City:"
        items={allCities}
        bind:value={filters.city}
        on:valueChanged={onCityChange}
      />
    </div>
    <div class:hidden={hideDistrictSelectBox}>
      <SelectBoxFilter 
        label="District:"
        items={allDistricts}
        bind:value={filters.district}
      />
    </div>
    <MinMaxFilter 
      label="Price (CAD):" 
      bind:min={filters.minPrice} 
      bind:max={filters.maxPrice}
      bind:valid={minmaxValuesValid.price}
    />
    <MinMaxFilter 
      label="Floor area (m2):" 
      bind:min={filters.minFloorArea} 
      bind:max={filters.maxFloorArea} 
      bind:valid={minmaxValuesValid.floorArea}
    />
    <MinMaxFilter 
      label="Constr. Year:" 
      bind:min={filters.minConstructionYear} 
      bind:max={filters.maxConstructionYear} 
      bind:valid={minmaxValuesValid.constructionYear}
    />
    <MinMaxFilter 
      label="Rooms:" 
      bind:min={filters.minRooms} 
      bind:max={filters.maxRooms} 
      bind:valid={minmaxValuesValid.noRooms}
    />
    <MinMaxFilter 
      label="Bedrooms:" 
      bind:min={filters.minBedrooms} 
      bind:max={filters.maxBedrooms} 
      bind:valid={minmaxValuesValid.noBedrooms}
    />
    <MinMaxFilter 
      label="Bathrooms:" 
      bind:min={filters.minBathrooms} 
      bind:max={filters.maxBathrooms} 
      bind:valid={minmaxValuesValid.noBathrooms}
    />
    <MinMaxFilter 
      label="Garages:" 
      bind:min={filters.minGarages} 
      bind:max={filters.maxGarages} 
      bind:valid={minmaxValuesValid.noGarages}
    />
    <MinMaxFilter 
      label="Parking lots:" 
      bind:min={filters.minParkingLots} 
      bind:max={filters.maxParkingLots} 
      bind:valid={minmaxValuesValid.noParkingLots}
    />
    <CheckboxFilter
      label="Only new buildings"
      bind:value={filters.onlyNew}
    />
    <SelectBoxFilter 
      label="WalkScore:"
      items={allWalkScoresDesc}
      values={allWalkScoreThresholds}
      bind:value={filters.walkScoreThreshold}
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
  <div class="flex flex-row justify-center sm:justify-end" class:hidden={!displayError}>
    <p class="text-red-500 font-bold text-sm text-center">Max values must be greater than or equal to min values</p>
  </div>
</section>
