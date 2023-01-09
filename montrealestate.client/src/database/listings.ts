import type { FiltersType } from 'src/types/Filters';
import type { ListingLong, ListingShort } from 'src/types/Listings';

export async function getAllCities() {
	return ['montreal', 'warsaw'];
}

export async function getAllDistricts(city: string) {
	if (city === '') {
		return [];
	}
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

export async function getListings(
	startFrom: number,
	count: number,
	filters: FiltersType,
): Promise<ListingShort[]> {
	const result: ListingShort[] = [];
	for (let i = 0; i < 10; i++) {
		result.push({
			id: i,
			imgUrl: 'https://picsum.photos/600/400',
			price: 400000,
			floorArea: 60,
			constructionYear: 2001,
			city: 'Montreal',
			district: 'West',
			address: '12 Grafton St.',
			categories: ['ruins'],
			noRooms: 4,
			isNew: true,
		});
	}
	return result;
}

export async function getListingDetails(listingId: number): Promise<ListingLong> {
	return {
		id: 1,
		imgUrl: 'https://picsum.photos/600/400',
		price: 400000,
		floorArea: 60,
		constructionYear: 2001,
		city: 'Montreal',
		district: 'West',
		address: '12 Grafton St.',
		noRooms: 4,
		isNew: true,
		categories: ['ruins'],
		noBedrooms: 1,
		noBathrooms: 1,
		noGarages: 1,
		noParkingLots: 4,
		googleMapsAddressLink: 'https://maps.google.com',
		walkScore: 99,
		walkScoreMapped: 'walkscore 1',
		description: 'Glorious ruins in the heart of Montreal! Buy today!!!!',
	};
}
