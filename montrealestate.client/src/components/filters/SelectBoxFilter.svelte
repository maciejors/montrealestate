<script lang="ts">
  import { createEventDispatcher } from "svelte";

  export let label: string = '';
  export let items: any[];
  export let values: any[] = items;
  export let value: any | null = null;

  interface SelectBoxOption {
    label: any;
    value: any;
  }

  let options: SelectBoxOption[] = [];
  $: {
    options = [];
    for (let i = 0; i < items.length; i++) {
      const value = values[i] ?? items[i]
      options.push({ label: items[i], value: value });
    }   
  }

  const dispatch = createEventDispatcher();
</script>

<div class="flex flex-row items-center gap-x-2">
  <p class="inline-block">{ label }</p>
  <select 
    name="selectBox"
    bind:value={value} 
    on:change={() => dispatch('valueChanged')} 
    class="py-0 h-8 cursor-pointer rounded border-1 focus:border-primary focus:ring-primary
      hover:bg-gray-100 w-full max-w-max"
  >
    {#each options as option}
      <option value={option.value}>{ option.label }</option>
    {/each}
  </select>
</div>