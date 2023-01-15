export interface SearchOptionsType {
	startFrom: number;
	count: number;
	sortBy: string;
	sortAscending: boolean;
}

export class SearchOptionsClass implements SearchOptionsType {
	startFrom = 0;
	count = 10;
	sortBy = 'price';
	sortAscending = true;
}
