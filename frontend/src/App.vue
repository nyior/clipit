<template>
  <div id="app">
    <NavbarComponent />

    <router-view />
  </div>
</template>

<script>
import NavbarComponent from "@/components/Navigation/Navbar.vue";

export default {
  name: "App",
  components: {
    NavbarComponent
  },

  data() {}
};
</script>

<style>
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
</style>
