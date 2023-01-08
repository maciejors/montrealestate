import type { FiltersType } from 'src/types/Filters';

export async function getAllCities() {
	return ['montreal', 'warsaw'];
}

export async function getAllDistricts(city: string) {
	if (city === 'warsaw') {
		return [];
	}
	return ['west', 'east'];
}

export async function getAllWalkScoresMapped() {
	return ['walkscore1', 'walkscore2'];
}

export async function getAllCategories() {
	return ['semi-detached', 'ruins', 'detached', 'terrace house', 'flat', 'mansion'];
}

export async function getListings(startFrom: number, count: number, filters: FiltersType) {
	return [];
}
