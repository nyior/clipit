<template>
  <div class="row px-5">
    <div class="col-12">

      <div 
        v-if="showRegularForm" 
        id="regular-form"
      >
        <RegularForm 
                    @hide-form="toggle" 
                    @on-submit="shortenUrl" 
                    :isLoading="isLoading"
        />
      </div>

      <div v-else id="advanced-form">
        <AdvancedForm 
                    @hide-form="toggle" 
                    @on-submit="shortenUrl" 
                    :isLoading="isLoading"
        />
      </div>

    </div>
  </div>
</template>

<script>
import { apiService } from "@/utils/api.service.js";
import { validateUrl, copiedToClipboard } from "@/utils/helper.js";
import RegularForm from "./RegularForm.vue";
import AdvancedForm from "./AdvancedForm.vue";
import Error from "@/components/Utils/Error.vue"

export default {
  name: "Form",

  data() {
    return {
      showRegularForm: true,
      isLoading: false
    };
  },

  components: {
    RegularForm,
    AdvancedForm,
    Error
  },

  methods: {
    toggle() {
      this.showRegularForm = !this.showRegularForm;
    },

    shortenUrl(payload) {
      this.isLoading = true;
      let shorten_url_endpoint = `api/v1/shortcode`;

      let method = "POST";

      let isValidUrl = validateUrl(payload.longUrl);
      
      if (isValidUrl) {
        apiService(shorten_url_endpoint, method, payload)
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
      } 
    }
  }
};
</script>

<style scoped>
p {
  color: #007f37;
}
</style>
