<svelte:head>
  <title>{ pageTitle }</title>
</svelte:head>

<script lang="ts">
  import { page } from "$app/stores";
  import { onMount } from "svelte";
  import { error } from "@sveltejs/kit";
	import type { ListingLong } from "../../../types/Listings";
	import { getListingDetails } from "../../../database/listings";
	import Container from "../../../components/Container.svelte";
	import InlineTextSeparator from "../../../components/InlineTextSeparator.svelte";

  let listing: ListingLong;
  $: pageTitle = listing === undefined ? 'Listing details' : `${listing.address}, ${listing.city}`;
  // an empty string if a city has no districts, otherwise ", {district-name}"
  let districtPrefix: string;

  onMount(async () => {
    let id: number = Number.parseInt($page.params.id);
    if (Number.isNaN(id)) {
      throw error(400, { message: 'Invalid listing ID' });
    }
    listing = await getListingDetails(id);
    districtPrefix = listing.district === '' ? '' : `${listing.district}, `
  });
</script>

{#if listing !== undefined}
  <Container>
    <div class="card my-10 flex flex-col pb-4">
      <section class="flex flex-col relative
        lg:grid lg:grid-cols-12 lg:bg-gray-50"
      >
        <a href="/listings" class="btn btn-secondary absolute top-2 left-2 w-fit">&lt Back</a>
        <div class="col-span-7 rounded-tl overflow-hidden">
          <img src={ listing.imgUrl } alt={ listing.imgUrl }>
        </div>
        <div class="col-span-5 flex flex-col pt-6 px-6">
          <p class="text-3xl mb-2">${ listing.price }</p>
          <p class="text-xl">{ listing.address }</p>
          <p class="text-xl">{ districtPrefix }{ listing.city }</p>
          <div class="flex flex-row text-gray-500 flex-wrap gap-x-1 items-center my-2">
            <p>{ listing.floorArea } m2</p>
            <InlineTextSeparator />
            <p>{ listing.noRooms } room(s)</p>
            {#each listing.categories as category}
              <InlineTextSeparator />
              <p>{ category }</p>
            {/each}
          </div>
          <a href={ listing.googleMapsAddressLink } class="btn btn-primary w-fit mt-2">View on Google Maps</a>
        </div>
      </section>
      <div class="mx-6 my-5 border-t border-gray-200 lg:mt-0 lg:mb-3 lg:mx-0"></div>
      <section class="px-6">
        <h3 class="section-title">More details:</h3>
        <ul>
          <li>
            <p><b>{ listing.noRooms } room(s)</b>, including:</p>
            <ul>
              <li><b>{ listing.noBathrooms } bathroom(s)</b></li>
              <li><b>{ listing.noBedrooms } bedroom(s)</b></li>
            </ul>
          </li>
          <li><b>{ listing.noParkingLots } parking lot(s)</b></li>
          <li><b>{ listing.noGarages } garage(s)</b></li>
          {#if listing.isNew}
            <li><b>New building</b></li>
          {/if}
          <li>Construction year: <b>{ listing.constructionYear }</b></li>
          <li>WalkScore: { listing.walkScore }/100 <b>({ listing.walkScoreMapped })</b></li>
        </ul>
      </section>
      <div class="mx-6 my-5 border-t border-gray-200 lg:my-3"></div>
      <section class="px-6">
        <h3 class="section-title">Description:</h3>
        <p>{ listing.description }</p>
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