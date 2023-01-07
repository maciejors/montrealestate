<script lang="ts">
  import { createEventDispatcher } from "svelte";

  export let items: string[];
  export let value: string | null = null;

  const dispatch = createEventDispatcher();
</script>

<select 
  name="selectBox" 
  bind:value={value} 
  on:change={() => dispatch('valueChanged')} 
  class="py-0 h-8 rounded border-1 focus:border-primary"
>
  {#each items as item}
    <option value={item}>{ item }</option>
  {/each}
</select>