export interface ListingShort {
	id: number;
	imgUrl: string;
	price: number;
	floorArea: number;
	constructionYear: number;
	city: string;
	district: string;
	address: string;
	noRooms: number;
	isNew: boolean;
}

export interface ListingLong extends ListingShort {
	categories: string[];
	noBedrooms: number;
	noBathrooms: number;
	noGarages: number;
	noParkingLots: number;
	googleMapsAddressLink: string;
	walkScore: number;
	walkScoreMapped: string;
	description: string;
}
