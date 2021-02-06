<template>
  <nav class="navbar navbar-expand-lg py-3 fixed px-5 shadow">
    <router-link :to="{ name: 'home' }" class="dynamic-brand navbar-brand">
      shortster
    </router-link>

    <router-link :to="{ name: 'url-list' }" class="ml-auto">
      <button class="btn">
        all urls
      </button>
    </router-link>
  </nav>
</template>

<script>
export default {
  name: "Navbar",

  data() {
    return {};
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Paytone+One&display=swap");

.navbar-brand {
  font-size: 3rem;
  color: #007f37;
  font-family: "Paytone One", sans-serif;
}

@media screen and (max-width: 600px) {
}
</style>
