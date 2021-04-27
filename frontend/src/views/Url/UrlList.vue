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
      class="col-12 col-md-6 mr-md-auto ml-md-auto space-up text-center"
    >
      <Loader />
    </div>
  </div>

  <div v-if="urls.length > 0 && !isLoading">
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
import { apiService } from "@/utils/api.service.js";
import Url from "@/components/Url/Url.vue";
import Loader from "@/components/Utils/Loader.vue";

export default {
  name: "url-list",

  components: {
    Url,
    Loader
  },

  data() {
    return {
      isLoading: false,
      urls: []
    };
  },

  methods: {
    getUrlsList() {
      this.isLoading = true;
      let urls_endpoint = `api/v1/urls`;

      let method = "GET";

      apiService(urls_endpoint, method)
        .then(data => {
          this.isLoading = false;
          this.urls = [...data.urls];
        })
        .catch(error => {
          this.isLoading = false;
        });
    }
  },

  mounted: function() {
    document.title = "CLIPIT | all-urls";
    this.getUrlsList();
  }
};
</script>
