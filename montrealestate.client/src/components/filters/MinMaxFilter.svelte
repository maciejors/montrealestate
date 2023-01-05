<script lang="ts">
  export let label: string;
  export let min: number | null = null;
  export let max: number | null = null;
</script>

<div class="flex flex-row items-center gap-x-2">
  <p class="inline-block">{ label }</p>
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

<style lang="postcss">
  .text-field {
    @apply w-28 h-8 rounded focus:border-2 focus:border-primary;
  }
</style>