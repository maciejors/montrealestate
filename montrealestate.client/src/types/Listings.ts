export interface Listing {
	id: number;
	photoUrl: string;
	price: number;
	livingArea: number;
	constructionYear: number;
	city: string;
	district: string;
	address: string;
	postalCode: string;
	noRooms: number;
	isNew: boolean;
	noBedrooms: number;
	noBathrooms: number;
	noGarages: number;
	noParkingLots: number;
	noFireplaces: number;
	noPools: number;
	googleMapAddressLink: string;
	walkScore: number;
	walkScoreMapped: string;
	longDescription: string;
	contactEmail: string;
	contactPhoneNumber: string;
}
