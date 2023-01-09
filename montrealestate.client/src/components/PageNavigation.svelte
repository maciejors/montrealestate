<script lang="ts">
  import { createEventDispatcher } from "svelte";

  const dispatch = createEventDispatcher();

  export let totalCount: number;
  export let startFrom: number;
  export let count: number;

  $: pageNo = startFrom / count + 1;
  $: totalPages = Math.ceil(totalCount / count);

  function prevPage() {
    dispatch('pageChanged');
    if (startFrom >= count) {
      startFrom -= count;
    }
  }

  function nextPage() {
    dispatch('pageChanged');
    if (startFrom + count < totalCount) {
      startFrom += count;
    }
  }
</script>

<nav class="flex flex-row gap-x-2">
  <button class="underline text-primary hover:text-primary-hover active:text-primary-active disabled:text-primary-disabled disabled:no-underline"
    on:click={prevPage}
    disabled={startFrom === 0}
  >&lt prev</button>
  <p>Page { pageNo }/{ totalPages }</p>
  <button class="underline text-primary hover:text-primary-hover active:text-primary-active disabled:text-primary-disabled disabled:no-underline"
    on:click={nextPage}
    disabled={startFrom + count >= totalCount}
  >next ></button>
</nav>
