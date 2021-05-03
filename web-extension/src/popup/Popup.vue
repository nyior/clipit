<template>
  <div>
    <Navbar />
    <router-view></router-view>
    <Footer />
  </div>
</template>

<script>
import Navbar from '@/components/Navigation/Navbar.vue'
import Footer from '@/components/Navigation/Footer.vue'

export default {
  name: 'popup',
  components: {
    Navbar,
    Footer
  },

  beforeCreate: function () {
    chrome.tabs.query({ currentWindow: true, active: true }, function (tabs) {
        // store.updateTabUrl(tabs[0].url)
        window.localStorage.setItem('tabUrl', tabs[0].url)
    })
  }
}
</script>

<style lang="scss">

html {
  width: 450px;
  height: 500px;
}
</style>
