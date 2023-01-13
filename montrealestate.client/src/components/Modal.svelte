<script lang="ts">
  export let visible: boolean;
</script>

<div class="fixed top-0 left-0 right-0 w-full h-full 
  flex flex-col justify-center items-center
  bg-black/40"
  class:hidden={!visible}
>
  <slot></slot>
</div>