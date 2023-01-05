<script lang="ts">
  import Card from "../shared/Card.svelte";
  import Container from "../shared/Container.svelte";
</script>

<main class="bg-home bg-auto">
  <Container>
    <div>
      {#each [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] as i}
        <Card>
          <p>this is a card</p>
          <a class="btn" href="">a plain button</a>
          <a class="btn btn-primary" href="">primary button</a>
          <a class="btn btn-secondary" href="">secondary button</a>
        </Card>
      {/each}
    </div>
  </Container>
</main>