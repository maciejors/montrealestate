import type { FiltersType } from 'src/types/Filters';
import type { ListingLong, ListingShort } from 'src/types/Listings';
import type { SearchOptionsType } from 'src/types/SearchOptions';

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

export async function getListings(
	filters: FiltersType,
	options: SearchOptionsType,
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
		noBedrooms: 1,
		noBathrooms: 1,
		noGarages: 1,
		noParkingLots: 4,
		googleMapsAddressLink: 'https://maps.google.com',
		walkScore: 99,
		walkScoreMapped: 'walkscore 1',
		description: 'Glorious ruins in the heart of Montreal! Buy today!!!!',
		contactEmail: 'ilovebees@mail.com',
		contactPhoneNumber: '+353 123 456 789',
	};
}
