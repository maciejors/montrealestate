<script lang="ts">
  export let label: string;
  export let min: number | null = null;
  export let max: number | null = null;
  export let valid: boolean = true;

  $: valid = (min !== null && max !== null) ? min <= max : true;
</script>

<div class="flex flex-row justify-between items-center gap-x-2">
  <p>{ label }</p>
  <div class="flex flex-row gap-x-2">
    <input
      type="number" 
      placeholder="Min" 
      bind:value={ min }
      class="text-field"
      class:invalid-text-field={!valid}
    >
    <input 
      type="number" 
      placeholder="Max" 
      bind:value={ max }
      class="text-field"
      class:invalid-text-field={!valid}
    >
  </div>
</div>

<style lang="postcss">
  .text-field {
    @apply w-20 h-8 rounded sm:w-28 focus:border focus:border-primary focus:ring-primary hover:bg-gray-100;
  }

  .invalid-text-field {
    @apply text-field border-2 border-red-500;    
  }
</style>