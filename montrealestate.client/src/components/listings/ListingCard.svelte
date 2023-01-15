<script lang="ts">
  import { createEventDispatcher } from "svelte";
	import type { Listing } from "../../types/Listings";
  import InlineTextSeparator from "../InlineTextSeparator.svelte";

  export let listing: Listing;

  const dispatch = createEventDispatcher();

  // an empty string if a city has no districts, otherwise "{district-name}, "
  let districtPrefix = listing.district === '' ? '' : `${listing.district}, `
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="card flex flex-col overflow-hidden
  cursor-pointer"
  on:click={() => dispatch('click')}
>
  <img src={ listing.photoUrl } alt={ listing.photoUrl }>
  <div class="flex flex-col p-4">
    <p class="text-3xl mb-1">${ listing.price }</p>
    <p class="text-xl">
      { listing.address }, { districtPrefix }{ listing.city }
    </p>
    <div class="flex flex-row text-gray-500 flex-wrap gap-x-1 items-center mt-2">
      <p>{ listing.livingArea } m2</p>
      <InlineTextSeparator />
      <p>built in { listing.constructionYear }</p>
      {#if listing.noRooms > 0}
        <InlineTextSeparator />
        <p>{ listing.noRooms } room(s)</p>
      {/if}
      {#if listing.isNew}
        <InlineTextSeparator />
        <p>new building</p>
      {/if}
    </div>
  </div>
</div>