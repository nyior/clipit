<template>
  <nav class="navbar shadow navbar-expand-lg py-3 fixed px-5">
    <router-link :to="{ name: 'home' }" class="dynamic-brand navbar-brand">
      <i class="fa fa-scissors" aria-hidden="true">
        clipit
      </i>
    </router-link>

    <router-link :to="{ name: 'url-list' }" class="ml-auto">
      <button class="btn shadow">
       <i class="fa fa-list" aria-hidden="true"> 
           all urls
       </i>
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
  color: #ff0000;
  font-family: "Paytone One", sans-serif;
}

@media screen and (max-width: 600px) {
}
</style>
