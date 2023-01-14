<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import Modal from "../Modal.svelte";
  import CheckboxFilter from "./CheckboxFilter.svelte";

  interface CategoryFilterItem {
    name: string;
    selected: boolean;
  }

  export let categories: string[];
  // selected categories in currently applied filters
  // this prop is will be updated one the user accepts their selections
  export let appliedCategories: string[] = [...categories];

  const dispatch = createEventDispatcher();

  $: selectedItemsCount = appliedCategories.length;
  $: buttonLabel = `${selectedItemsCount} of ${categories.length} selected`
  // categories selected by the user
  let items: CategoryFilterItem[] = categories.map(catg => ({ name: catg, selected: appliedCategories.includes(catg) }));
  
  let modalVisible = false;
  let errorVisible = false;

  function showModal() {
    modalVisible = true;
    errorVisible = false;
    // reset items array to reflect currently applied filters
    items = categories.map(catg => ({ name: catg, selected: appliedCategories.includes(catg) }));
  }

  function onSelectNone() {
    items.forEach(item => item.selected = false);
    // refresh checkboxes
    items = [...items];
  }

  function onSelectAll() {
    items.forEach(item => item.selected = true);
    // refresh checkboxes
    items = [...items];
  }

  function cancel() {
    modalVisible = false;
  }

  function applyCategories() {
    let selectedCategories = items
      .filter(i => i.selected)
      .map(i => i.name);
    if (selectedCategories.length > 0) {
      modalVisible = false;
      appliedCategories = selectedCategories;
    } else {
      errorVisible = true;
    }
  }
</script>

<div class="flex flex-row items-center gap-x-2">
  <p>Categories:</p>
  <button class="btn border border-gray-500 bg-white hover:bg-gray-100 rounded px-2 h-8" on:click={showModal}>{ buttonLabel }</button>
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
    <div class="flex flex-row w-full justify-start text-sm text-red-500" class:hidden={!errorVisible}>
      <p>Please select at least one category</p>
    </div>
    <div class="grid grid-cols-2 md:grid-cols-3 gap-x-8 gap-y-4 my-4">
      {#each items as item (item.name)}
        <CheckboxFilter 
          label={item.name} 
          bind:value={item.selected}
        />
      {/each}
    </div>
    <div class="flex flex-row justify-end gap-x-4 items-center md:w-full">
      <button class="btn btn-secondary" on:click={onSelectNone}>Select none</button>
      <button class="btn btn-secondary" on:click={onSelectAll}>Select all</button>
      <button class="btn btn-primary" on:click={applyCategories}>Accept</button>
    </div>
  </div>
</Modal>