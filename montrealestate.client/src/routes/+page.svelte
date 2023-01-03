<script>
  import Card from "../shared/Card.svelte";
</script>

<style>
  /* background img: https://picsum.photos/id/223/200/300 */
</style>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
<div class="mx-10">
  <p>hello</p>
  <Card>
    <p>this is a card</p>
    <a class="btn" href="">a plain button</a>
    <a class="btn btn-primary" href="">primary button</a>
    <a class="btn btn-secondary" href="">secondary button</a>
  </Card>
</div>