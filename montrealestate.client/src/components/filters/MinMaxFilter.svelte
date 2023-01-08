<script lang="ts">
  export let label: string;
  export let min: number | null = null;
  export let max: number | null = null;
</script>

<div class="flex flex-row justify-between items-center gap-x-2">
  <p>{ label }</p>
  <div class="flex flex-row gap-x-2">
    <input
      type="number" 
      placeholder="Min" 
      bind:value={ min }
      class="text-field"
    >
    <input 
      type="number" 
      placeholder="Max" 
      bind:value={ max }
      class="text-field"
    >
  </div>
</div>

<style lang="postcss">
  .text-field {
    @apply w-28 h-8 rounded focus:border focus:border-primary focus:ring-primary hover:bg-gray-100;
  }
</style>