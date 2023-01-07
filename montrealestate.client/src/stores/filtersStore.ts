import type Filters from 'src/interfaces/Filters';
import { writable } from 'svelte/store';

const filters: Filters = {
	city: null,
	district: null,
	categories: null,
	minPrice: null,
	maxPrice: null,
	minFloorArea: null,
	maxFloorArea: null,
	minConstructionYear: null,
	maxConstructionYear: null,
	minRooms: null,
	maxRooms: null,
	minBedrooms: null,
	maxBedrooms: null,
	minBathroomsWithShower: null,
	maxBathroomsWithShower: null,
	minBathroomsWithBath: null,
	maxBathroomsWithBath: null,
	minGarages: null,
	maxGarages: null,
	minParkingLots: null,
	maxParkingLots: null,
	isNew: null,
	walkScoreMapped: null,
};
export const filtersStore = writable(filters);
