<script lang="ts">
  export let label: string;
  export let href: string;
</script>

<a href={ href }
  class="cursor-pointer
    text-gray-500 border-b-2 border-transparent
    hover:text-primary-hover hover:border-b-2 hover:border-primary-hover
    active:text-primary-active active:border-b-2 active:border-primary-active
    mx-4"
>
  { label }
</a>
