<template>
  <div class="row px-3">
    <div class="col-12">

      <div
        v-if="showRegularForm"
        id="regular-form"
      >
        <RegularForm
                    @hide-regular-form="toggle"
                    @on-submit="shortenUrl"
                    :isLoading="isLoading"
        />

      </div>

      <div v-else id="advanced-form">
        <AdvancedForm
                    @show-regular-form="toggle"
                    @on-submit="shortenUrl"
                    :isLoading="isLoading"
        />
      </div>

    </div>
  </div>
</template>

<script>
import { apiService } from '@/utils/api.service.js'
import { validateUrl, copiedToClipboard } from "@/utils/helpers.js";

import RegularForm from './RegularForm.vue'
import AdvancedForm from './AdvancedForm.vue'

export default {
  name: 'Form',

  data () {
    return {
      showRegularForm: true,
      isLoading: false
    }
  },

  components: {
    RegularForm,
    AdvancedForm
  },

  methods: {
    toggle () {
      this.showRegularForm = !this.showRegularForm
    },

    shortenUrl (payload) {
      this.isLoading = true
      const shortenUrlEndpoint = 'api/v1/shortcode'

      const method = 'POST'

      let isValidUrl = validateUrl(payload.longUrl);
      
      if (isValidUrl) {
        apiService(shortenUrlEndpoint, method, payload)
        .then(data => {
          this.isLoading = false;
          this.$emit("on-submit", data);

          if (copiedToClipboard(data.shortcode)) {
            this.$emit('show-copied-to-clipboard-toaster')
          }

        //save response data to browser storage
          window.localStorage.setItem("longUrl", data.longUrl);
          window.localStorage.setItem("shortcode", data.shortcode);
        })
        .catch(error => {
          this.isLoading = false;
        }); 
      }else{
        this.isLoading = false;
        this.$emit('invalid-url')
      } 
    }
  }
}
</script>

<style scoped>
p {
  color: #007f37;
}
</style>
