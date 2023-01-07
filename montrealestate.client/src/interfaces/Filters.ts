export default interface Filters {
	city: string | null;
	district: string | null;
	categories: string[] | null;
	minPrice: number | null;
	maxPrice: number | null;
	minFloorArea: number | null;
	maxFloorArea: number | null;
	minConstructionYear: number | null;
	maxConstructionYear: number | null;
	minRooms: number | null;
	maxRooms: number | null;
	minBedrooms: number | null;
	maxBedrooms: number | null;
	minBathroomsWithShower: number | null;
	maxBathroomsWithShower: number | null;
	minBathroomsWithBath: number | null;
	maxBathroomsWithBath: number | null;
	minGarages: number | null;
	maxGarages: number | null;
	minParkingLots: number | null;
	maxParkingLots: number | null;
	isNew: boolean | null;
	walkScoreMapped: string | null;
}
