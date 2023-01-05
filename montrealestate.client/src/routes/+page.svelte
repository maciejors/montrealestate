<script lang="ts">
  import Filters from "../components/filters/Filters.svelte";
  import Container from "../shared/Container.svelte";
</script>

<main class="bg-home bg-auto">
  <Container>
    <h1 class="text-3xl text-white font-bold pb-4">Montreal is Real</h1>
    <div class="card p-4">
      <Filters />
    </div>
  </Container>
</main>