import { SearchOptionsClass, type SearchOptionsType } from '../types/SearchOptions';
import { writable } from 'svelte/store';

const searchOptions: SearchOptionsType = new SearchOptionsClass();
export const searchOptionsStore = writable(searchOptions);
