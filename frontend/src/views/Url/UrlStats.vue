<template>
  <div class="row px-5 text-left hero-container">
    <div
      v-if="isLoading"
      class="col-12 col-md-6 ml-md-auto mr-md-auto text-center"
    >
      <p>
        ...loading url stats...
      </p>
    </div>

    <div v-else class="col-12 col-md-6 ml-md-auto mr-md-auto p-4 card">
      <h3 class="mb-5 text-center">statistics for your url</h3>
      <hr />
      <div>
        <small>
          date created:
          {{ dateCreated }}
        </small>
      </div>

      <div>
        <small>
          last accessed:
          {{ lastAccessed }}
        </small>
      </div>

      <div>
        <small>
          number of visits:
          {{ hits }}
        </small>
      </div>

      <hr />
      <p>
        <router-link :to="{ name: 'home' }">
          <i class="fa fa-arrow-left" aria-hidden="true"> </i>
          back to home
        </router-link>
      </p>
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
  name: "url-stats",

  props: {
    shortcode: {
      type: String,
      required: true
    }
  },

  data() {
    return {
      isLoading: false,
      lastAccessed: null,
      dateCreated: null,
      hits: null
    };
  },

  methods: {
    getUrlStats() {
      this.isLoading = true;
      let url_stats_endpoint = `api/v1/${this.shortcode}/stats`;

      let method = "GET";

      apiService(url_stats_endpoint, method)
        .then(data => {
          this.isLoading = false;
          this.lastAccessed = data.lastAccessed;
          this.dateCreated = data.dateCreated;
          this.hits = data.hits;
        })
        .catch(error => {
          this.isLoading = false;
        });
    }
  },

  mounted: function() {
    document.title = "Shortster | stats";
    this.getUrlStats();
  }
};
</script>
