<template>
  <div class="row px-5 text-left hero-container">
    <div
      v-if="urls.length <= 0 && !isLoading"
      class="col-12 col-md-6 ml-md-auto mr-md-auto text-center"
    >
      <p>
        no urls found! click the button below to shorten your first url
      </p>

      <router-link :to="{ name: 'home' }">
        <button class="btn">
          go to
          <i class="fa fa-arrow-right" aria-hidden="true"> </i>
        </button>
      </router-link>
    </div>

    <div
      v-if="isLoading"
      class="col-12 col-md-6 ml-md-auto mr-md-auto text-center"
    >
      <p>
        ...loading all your urls...
      </p>
    </div>

    <div
      v-else
      v-for="url in urls"
      :key="url.shortcode"
      class="col-12 col-md-6 ml-md-auto mr-md-auto text-center"
    >
      <Url :url="url" />
    </div>
  </div>
</template>

<style scoped>
@media only screen and (max-width: 600px) {
}
</style>

<script>
import { apiService } from "@/utils/api.service.js";

export default {
  name: "url-list",

  data() {
    return {
      isLoading: false,
      urls: []
    };
  },

  methods: {
    getUrlStats() {
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
    document.title = "Shortster | all-urls";
    this.getUrlStats();
  }
};
</script>
