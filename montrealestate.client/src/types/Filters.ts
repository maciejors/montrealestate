export interface FiltersType {
	city: string;
	district: string;
	categories: string[];
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
	minBathrooms: number | null;
	maxBathrooms: number | null;
	minGarages: number | null;
	maxGarages: number | null;
	minParkingLots: number | null;
	maxParkingLots: number | null;
	onlyNew: boolean;
	walkScoreMapped: string | null;
}

export class FiltersClass implements FiltersType {
	city: string = '';
	district: string = '';
	categories: string[] = [];
	minPrice: number | null = null;
	maxPrice: number | null = null;
	minFloorArea: number | null = null;
	maxFloorArea: number | null = null;
	minConstructionYear: number | null = null;
	maxConstructionYear: number | null = null;
	minRooms: number | null = null;
	maxRooms: number | null = null;
	minBedrooms: number | null = null;
	maxBedrooms: number | null = null;
	minBathrooms: number | null = null;
	maxBathrooms: number | null = null;
	minGarages: number | null = null;
	maxGarages: number | null = null;
	minParkingLots: number | null = null;
	maxParkingLots: number | null = null;
	onlyNew: boolean = false;
	walkScoreMapped: string | null = null;
}
