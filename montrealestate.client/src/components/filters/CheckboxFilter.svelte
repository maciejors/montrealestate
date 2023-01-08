<script lang="ts">
  export let label: string = '';
  export let value: boolean = true;
</script>

<div class="flex flex-row items-center gap-x-2">
  <input 
    type="checkbox" bind:checked={value}
    class="py-0 h-6 w-6 rounded border-1
      hover:bg-gray-100
      focus:ring-0 focus:ring-offset-0
      transition duration-200 cursor-pointer
      text-primary hover:text-primary-hover"
  >
  <p class="inline-block">{ label }</p>
</div>