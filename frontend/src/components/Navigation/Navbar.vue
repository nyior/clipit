<template>
  <nav class="navbar shadow navbar-expand-lg py-3 fixed px-5">
    <router-link :to="{ name: 'home' }" class="dynamic-brand navbar-brand">
      <i class="fa fa-scissors" aria-hidden="true">
        clipit
      </i>
    </router-link>

    <router-link :to="{ name: 'url-list' }" class="ml-auto">
      <button class="btn shadow">
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
  color: #e9492e;
  font-family: "Paytone One", sans-serif;
}

@media screen and (max-width: 600px) {
}
</style>
