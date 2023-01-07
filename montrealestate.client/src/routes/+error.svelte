<svelte:head>
  <title>Oopsie!</title>
</svelte:head>

<script lang="ts">
  import { page } from '$app/stores';
  import Container from '../components/Container.svelte';
</script>

<Container>
  <div class="card flex flex-col items-center gap-y-2">
    <h1 class="text-3xl">Something went wrong :/</h1>
    <p class="text-center">
      <span class="font-bold">{$page.status}:</span>
      {$page.error?.message}
    </p>
  </div>
</Container>
