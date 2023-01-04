<script lang="ts">
  import "../app.css";
  import type NavbarTileItem from "../interfaces/NavbarTileItem";
  import Navbar from "../components/Navbar.svelte";
  import Footer from "../components/Footer.svelte";

  const navbarItems: NavbarTileItem[] = [
    { id: 0, label: 'Home', href: '/' },
    { id: 1, label: 'About', href: '/about' },
  ];
</script>

<Navbar items={ navbarItems } />
<main class="flex flex-col justify-center items-center
  pt-10 px-6 sm:px-12 lg:px-20 xl:px-36"
>
  <slot />
</main>
<Footer />
