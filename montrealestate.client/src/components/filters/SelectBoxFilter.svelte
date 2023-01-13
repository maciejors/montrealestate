<script lang="ts">
  import { createEventDispatcher } from "svelte";

  export let label: string = '';
  export let items: string[];
  export let value: string | null = null;
  export let hidden: boolean = false;

  const dispatch = createEventDispatcher();
</script>

<div class="flex flex-row items-center gap-x-2" class:hidden={hidden}>
  <p class="inline-block">{ label }</p>
  <select 
    name="selectBox"
    bind:value={value} 
    on:change={() => dispatch('valueChanged')} 
    class="py-0 h-8 cursor-pointer rounded border-1 focus:border-primary focus:ring-primary
      hover:bg-gray-100"
  >
    {#each items as item}
      <option value={item}>{ item }</option>
    {/each}
  </select>
</div>