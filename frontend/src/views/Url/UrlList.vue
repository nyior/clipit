<template>
<div>
  <div class="row px-5 text-left hero-container">
    <div
      v-if="urls.length <= 0 && !isLoading"
      class="col-12 col-md-6 ml-md-auto mr-md-auto text-center"
    >
      <p>
        coming soon! I ran into an issue with cookies, but I'm working on it.
        click button below to go to home.
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
      class="col-12 col-md-6 ml-md-auto mr-md-auto text-center"
    >
      <p>
        ...loading all your urls...
      </p>
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

export default {
  name: "url-list",

  components: {
    Url
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
    document.title = "Shortster | all-urls";
    this.getUrlsList();
  }
};
</script>
