<template>
<div>
  <div class="row px-5 text-left hero-container">
    <div
      class="col-12  text-center"
    >
        <h4>All the URLs you had worked with</h4>
    </div>
    <div
      v-if="urls.length <= 0 && !isLoading"
      class="col-12 text-center"
    >
      <p>
        no URLS found!
      </p>

      <router-link :to="{ name: 'home' }">
        <button class="btn">
          <i class="fa fa-arrow-left" aria-hidden="true"> </i>
          go to
        </button>
      </router-link>
    </div>

    <div
      v-if="isLoading"
      class="col-12 space-up text-center"
    >
      <p>...loading...</p>
    </div>
  </div>

  <div class="col-12 mt-3 text-left" v-if="urls.length > 0 && !isLoading">
      <div
        v-for="url in urls"
        :key="url.shortcode"
      >
        <Url :url="url" />
      </div>
  </div>
</div>
</template>

<style scoped>
@media only screen and (max-width: 600px) {
}
</style>

<script>
import { apiService } from '@/utils/api.service.js'
import Url from '@/components/Utils/Url.vue'

export default {
  name: 'url-list',

  components: {
    Url
  },

  data () {
    return {
      isLoading: false,
      urls: []
    }
  },

  methods: {
    getUrlsList () {
      this.isLoading = true
      const urlsEndpoint = 'api/v1/urls'

      const method = 'GET'

      apiService(urlsEndpoint, method)
        .then(data => {
          this.isLoading = false
          this.urls = [...data.urls]
        })
        .catch(error => {
          this.isLoading = false
          console.log(error)
        })
    }
  },

  mounted: function () {
    document.title = 'Shortster | all-urls'
    this.getUrlsList()
  }
}
</script>
