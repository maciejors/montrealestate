<script lang="ts">
  export let items: string[];
  export let selectedItems: string[] = items;

  $: buttonLabel = `${selectedItems.length}/${items.length} selected`
</script>

<div class="flex flex-row items-center gap-x-2">
  <p>Categories:</p>
  <button class="btn border border-gray-500 bg-white rounded w-32 h-8">{ buttonLabel }</button>
</div>