<script lang="ts">
  import { createEventDispatcher } from "svelte";
	import type { ListingShort } from "../../types/Listings";
  import InlineTextSeparator from "../InlineTextSeparator.svelte";

  export let listing: ListingShort;

  const dispatch = createEventDispatcher();

  let districtSuffix = listing.district === '' ? '' : `, ${listing.district}`
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="card flex flex-col overflow-hidden
  cursor-pointer"
  on:click={() => dispatch('click')}
>
  <img src={ listing.imgUrl } alt={ listing.imgUrl }>
  <div class="flex flex-col p-4">
    <p class="text-xl font-bold">
      { listing.address }, { listing.city }{ districtSuffix }
    </p>
    <p class="text-2xl">${ listing.price }</p>
    <div class="flex flex-row text-gray-500 flex-wrap gap-x-1 items-center mt-2">
      <p>{ listing.floorArea } m2</p>
      <InlineTextSeparator />
      <p>built in { listing.constructionYear }</p>
      <InlineTextSeparator />
      <p>{ listing.noRooms } rooms</p>
      <InlineTextSeparator />
      {#if listing.isNew}
        <p>new building</p>
      {/if}
    </div>
  </div>
</div>