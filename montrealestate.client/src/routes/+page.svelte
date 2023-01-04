<script lang="ts">
  import Card from "../shared/Card.svelte";
</script>

<style>
  /* background img: https://picsum.photos/id/223/1920/1080 */
</style>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
<div>
  <p>hello</p>
  <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Facere consequuntur voluptatibus est odio! Dicta, fuga. Quisquam, dolorum. Aspernatur eveniet autem nesciunt ipsam fugit, pariatur facere, accusantium quod asperiores quo sapiente.</p>
  {#each [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] as i}
    <Card>
      <p>this is a card</p>
      <a class="btn" href="">a plain button</a>
      <a class="btn btn-primary" href="">primary button</a>
      <a class="btn btn-secondary" href="">secondary button</a>
    </Card>
  {/each}
</div>