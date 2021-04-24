<template>
  <div class="row px-5 text-left hero-container">
    <div
      v-if="isLoading"
      class="col-12 text-center"
    >
      <p>...loading...</p>
    </div>

    <div v-else class="col-12 p-4 shadow card">
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
import { apiService } from '@/utils/api.service.js'

export default {
  name: 'url-stats',

  props: {
    shortcode: {
      type: String,
      required: true
    }
  },

  data () {
    return {
      isLoading: false,
      lastAccessed: null,
      dateCreated: null,
      hits: null
    }
  },

  methods: {
    getUrlStats () {
      this.isLoading = true
      const urlStatsEndpoint = `api/v1/${this.shortcode}/stats`

      const method = 'GET'
      apiService(urlStatsEndpoint, method)
        .then(data => {
          this.lastAccessed = data.lastAccessed
          this.dateCreated = data.dateCreated
          this.hits = data.hits
          this.isLoading = false
        })
        .catch(error => {
          this.isLoading = false
          console.log(error)
        })
    },

    back () {
      this.$router.back()
    }
  },

  mounted: function () {
    document.title = 'Shortster | stats'
    this.getUrlStats()
  }
}
</script>
