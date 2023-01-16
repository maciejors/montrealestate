<svelte:head>
  <title>{ pageTitle }</title>
</svelte:head>

<script lang="ts">
  import { page } from "$app/stores";
  import { onMount } from "svelte";
  import { error } from "@sveltejs/kit";
	import type { Listing } from "../../../types/Listings";
	import { getListingDetails } from "../../../database/listings";
	import Container from "../../../components/Container.svelte";
	import InlineTextSeparator from "../../../components/InlineTextSeparator.svelte";

  let listing: Listing;
  $: pageTitle = listing === undefined ? 'Listing details' : `${listing.address}, ${listing.city}`;
  // an empty string if a city has no districts, otherwise ", {district-name}"
  let districtPrefix: string;

  onMount(async () => {
    let id: number = Number.parseInt($page.params.id);
    if (Number.isNaN(id)) {
      throw error(400, { message: 'Invalid listing ID' });
    }
    let listingOrNull = await getListingDetails(id);
    if (listingOrNull === null) {
      throw error(404, { message: 'Listing not found' });
    }
    listing = listingOrNull;
    districtPrefix = listing.district === '' ? '' : `${listing.district}, `;    
  });
</script>

{#if listing !== undefined}
  <Container>
    <div class="card my-10 flex flex-col pb-4 max-w-5xl">
      <section class="flex flex-col relative
        lg:grid lg:grid-cols-12 lg:bg-gray-50"
      >
        <a href="/listings" class="btn btn-secondary absolute top-2 left-2 w-fit">&lt Back</a>
        <div class="col-span-7 rounded-t lg:rounded-none lg:rounded-tl overflow-hidden">
          <img src={ listing.photoUrl } alt={ listing.photoUrl }>
        </div>
        <div class="col-span-5 flex flex-col pt-6 px-6">
          <p class="text-3xl mb-2">${ listing.price }</p>
          <p class="text-xl">{ listing.address }</p>
          <p class="text-xl">{ districtPrefix }{ listing.city }</p>
          <div class="flex flex-row text-gray-500 flex-wrap gap-x-1 items-center my-2">
            <p>{ listing.livingArea } m2</p>
            {#if listing.noRooms > 0}
              <InlineTextSeparator />
              <p>{ listing.noRooms } room(s)</p>              
            {/if}
          </div>
          {#if listing.googleMapAddressLink !== ''}
            <a href={ listing.googleMapAddressLink } class="btn btn-primary w-fit mt-2">View on Google Maps</a>
          {/if}
        </div>
      </section>
      <div class="mx-6 my-5 border-t border-gray-200 lg:mt-0 lg:mb-3 lg:mx-0"></div>
      <section class="px-6">
        <h3 class="section-title">More details:</h3>
        <ul>
          {#if listing.noBathrooms > 0}
            <li><b>{ listing.noBathrooms } bathroom(s)</b></li>
          {/if}
          {#if listing.noBedrooms > 0}
            <li><b>{ listing.noBedrooms } bedroom(s)</b></li>
          {/if}
          {#if listing.noRooms > 0}
            <li><b>{ listing.noRooms } room(s)</b></li>
          {/if}
          {#if listing.noParkingLots > 0}
            <li><b>{ listing.noParkingLots } parking lot(s)</b></li>
          {/if}
          {#if listing.noGarages > 0}
            <li><b>{ listing.noGarages } garages(s)</b></li>
          {/if}
          {#if listing.noFireplaces > 0}
            <li><b>{ listing.noFireplaces } fireplace(s)</b></li>
          {/if}
          {#if listing.noPools > 0}
            <li><b>{ listing.noPools } pool(s)</b></li>
          {/if}
          {#if listing.isNew}
            <li><b>New building</b></li>
          {/if}
          {#if listing.constructionYear !== 0}
            <li>Construction year: <b>{ listing.constructionYear }</b></li>
          {/if}
          <li>WalkScore: { listing.walkScore }/100 <b>({ listing.walkScoreMapped })</b></li>
        </ul>
      </section>
      <div class="mx-6 my-5 border-t border-gray-200 lg:my-3"></div>
      <section class="px-6">
        <h3 class="section-title">Description:</h3>
        <p>{ listing.longDescription }</p>
      </section>
      <div class="mx-6 my-5 border-t border-gray-200 lg:my-3"></div>
      <section class="px-6">
        <h3 class="section-title">Contact details:</h3>
        <ul>
          <li>email: <b>{ listing.contactEmail }</b></li>
          <li>phone: <b>{ listing.contactPhoneNumber }</b></li>
        </ul>
      </section>
    </div>
  </Container>
{/if}

<style lang="postcss">
  ul {
    @apply ml-8 list-disc;
  }
  .section-title {
    @apply text-2xl mb-2;
  }
</style>