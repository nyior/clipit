<template>
  <div class="row px-5 text-left hero-container">
    <div
      v-if="isLoading"
      class="col-12 col-md-6 ml-md-auto mr-md-auto text-center"
    >
      <Loader />
    </div>

    <div v-else class="col-12 col-md-6 ml-md-auto mr-md-auto p-4 shadow card">
      <h4 class="mb-5 text-center">how users had been interacting with this URL</h4>
      <hr />
      <table class="table borderless table-sm">
        <thead>
            <tr 
                class="text-left"
            >
                <th>created on</th>
                <th>last accessed</th>
                <th>visits</th>
            </tr>
        </thead>

        <tbody>
            <tr class="p-2">
                <td>
                        <small>
                            {{ dateCreated }}
                        </small>
                </td> 

                <td>
                    <small>
                        {{ lastAccessed }}
                    </small>
                </td> 

                <td>
                    <small>
                        {{ hits }}
                    </small>
                </td>     
            </tr>        
        </tbody>
      </table>

      <hr />
      <p @click="back">
        <i class="fa fa-arrow-left" aria-hidden="true"> </i>
        back 
      </p>
    </div>
  </div>
</template>

<style scoped>
    thead{
        letter-spacing: 1px;
        font-weight: bold;
        font-size: 1.2rem;
        background-color: #e9492e;
        color: white;
    }
</style>

<script>
import { apiService } from "@/utils/api.service.js";
import Loader from "@/components/Utils/Loader.vue";

export default {
  name: "url-stats",

  components: {
    Loader
  },

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
    },

    back() {
      this.$router.back();
    }
  },

  mounted: function() {
    document.title = "Shortster | stats";
    this.getUrlStats();
  }
};
</script>
