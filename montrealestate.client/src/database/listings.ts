import axios from 'axios';
import type { FiltersType } from 'src/types/Filters';
import type { Listing } from 'src/types/Listings';
import type { SearchOptionsType } from 'src/types/SearchOptions';

axios.defaults.baseURL = 'http://127.0.0.1:8000';

interface ListingsResponse {
	listings: Listing[];
	totalCount: number;
}

export async function getAllCities(): Promise<string[]> {
	let result: string[] = [];
	try {
		const response = await axios.get(`/api/cities`);
		result = response.data.items;
	} catch (e) {
		console.log(e);
	}
	return result;
}

export async function getAllDistricts(city: string): Promise<string[]> {
	let result: string[] = [];
	if (city === '' || city === undefined) {
		return result;
	}
	try {
		const response = await axios.get(`/api/districts`, {
			params: { city },
		});
		result = response.data.items ?? [];
	} catch (e) {
		console.log(e);
		return [];
	}
	return result;
}

export async function getListings(
	filters: FiltersType,
	options: SearchOptionsType,
): Promise<ListingsResponse> {
	let result: ListingsResponse = {
		listings: [],
		totalCount: 0,
	};
	try {
		if (filters.city === '') {
			filters.city = null;
		}
		if (filters.district === '') {
			filters.district = null;
		}
		const response = await axios.get(`/api/listings`, {
			params: {
				startFrom: options.startFrom,
				count: options.count,
				sortBy: options.sortBy,
				sortAscending: options.sortAscending,
				...filters,
			},
		});
		result.listings = response.data.listings;
		result.totalCount = response.data.totalCount;
	} catch (e) {
		console.log(e);
	}
	return result;
}

export async function getListingDetails(listingId: number): Promise<Listing | null> {
	let result: Listing | null = null;
	try {
		const response = await axios.get(`/api/listings/${listingId}`);
		result = response.data;
		if (result !== null) {
			result.photoUrl = 'https://picsum.photos/900/600';
		}
	} catch (e) {
		console.log(e);
	}
	return result;
}
