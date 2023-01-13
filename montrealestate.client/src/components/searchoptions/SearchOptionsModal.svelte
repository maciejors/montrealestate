<script lang="ts">
  import { onMount } from "svelte";
  import { createEventDispatcher } from "svelte";
  import Modal from "../Modal.svelte";
  import CheckboxFilter from "../filters/CheckboxFilter.svelte";
  import SelectBoxFilter from "../filters/SelectBoxFilter.svelte";
  import copy from "../../utils/copy";
	import { SearchOptionsClass, type SearchOptionsType } from "../../types/SearchOptions";

  let availableSorting = ['price', 'floor area'];
  let availableCounts = [10, 20, 30, 50];
  
  // defaultOptions contains CURRENTLY APPLIED options
  export let defaultOptions: SearchOptionsType;
  export let buttonLabel: string;

  // options variable contains VISIBLE OPTIONS which MAY NOT HAVE BEEN APPLIED YET
  let options: SearchOptionsType = new SearchOptionsClass();

  const dispatch = createEventDispatcher();

  onMount(async () => {
    options = copy(defaultOptions);
  });
  
  let modalVisible = false;

  function showModal() {
    modalVisible = true;
  }

  function cancel() {
    modalVisible = false;
    options = copy(defaultOptions);
  }

  function applySearchOptions() {
    modalVisible = false;
    dispatch('searchOptionsApplied', { searchOptions: options });
  }
</script>

<div class="flex flex-row items-center gap-x-2">
  <button class="btn btn-secondary border border-gray-500 bg-white hover:bg-gray-100 rounded px-2 h-8" on:click={showModal}>{ buttonLabel }</button>
</div>
<Modal visible={modalVisible}>
  <div class="card flex flex-col justify-center items-center p-4">
    <div class="w-full flex flex-row justify-between items-center">
      <p class="font-bold">Select categories:</p>
      <button 
        on:click={cancel}
        class="text-2xl mr-2 font-mono
        text-primary hover:text-primary-hover active:text-primary-active"
      >X</button>
    </div>
    <div class="flex flex-col items-center gap-4 my-4">
      <div class="flex flex-col sm:flex-row items-center gap-2">
        <SelectBoxFilter
          label="Sort by:"
          items={availableSorting}
          bind:value={options.sortBy}
        />
        <CheckboxFilter
          label="Ascending"
          bind:value={options.sortAscending}
        />
      </div>
      <SelectBoxFilter
        label="Listings per page:"
        items={availableCounts}
        bind:value={options.count}
      />
    </div>
    <div class="flex flex-row justify-end gap-x-4 items-center w-full">
      <button class="btn btn-primary" on:click={applySearchOptions}>Accept</button>
    </div>
  </div>
</Modal>