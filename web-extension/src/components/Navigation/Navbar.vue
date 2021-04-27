<template>
  <div>
    <nav class="navbar shadow-sm navbar-expand-lg py-2 fixed px-3">
        <router-link
                :to="{ name: 'home' }"
                class="dynamic-brand navbar-brand"
        >
          <i class="fa fa-scissors" aria-hidden="true">
              clipit
          </i>
        </router-link>
        <router-link
                :to="{ name: 'url-list' }"
                class="ml-auto"
        >
            <h3>
                <i
                    class="fa fa-bookmark"
                    aria-hidden="true"
                    title="view history"
                >
                </i>
            </h3>
        </router-link>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'navbar'
}
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Paytone+One&display=swap");

.navbar-brand {
  font-size: 2rem;
  color: #e9492e;
  font-family: "Paytone One", sans-serif;
}

.btn{
  letter-spacing: 1px;
  background-color: #e9492e;
  color: white !important;
  font-size: 1.4rem;
  text-align: center;
  width: 8rem;
  height: 4rem;
}
</style>
