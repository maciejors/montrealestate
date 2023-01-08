import type { FiltersType } from '../types/Filters';
import { FiltersClass } from '../types/Filters';
import { writable } from 'svelte/store';

const filters: FiltersType = new FiltersClass();
export const filtersStore = writable(filters);
