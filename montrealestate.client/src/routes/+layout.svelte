<script lang="ts">
  import "../app.postcss";
  import type NavbarTileItem from "../types/NavbarTileItem";
  import Navbar from "../components/nav/Navbar.svelte";
  import Footer from "../components/Footer.svelte";

  const navbarItems: NavbarTileItem[] = [
    { id: 0, label: 'Home', href: '/' },
    { id: 1, label: 'About', href: '/about' },
  ];
</script>

<Navbar items={ navbarItems } />
<main class="bg-gray-100">
  <slot />
</main>
<Footer />
