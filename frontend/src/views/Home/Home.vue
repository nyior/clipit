<template>
  <div class="container-fluid hero-container">
    
    <Form @on-submit="setUrl" />

    <div 
        class="space-up" 
        v-if="response !== null"
    >
      <div class="row text-center px-5">
          <div class="col-12">
              <h4>The most recent URL you worked with</h4>
          </div>
      </div>
      <Url :url="response" />
    </div>
    
  </div>
</template>

<style scoped>
@media only screen and (max-width: 600px) {
}
</style>

<script>
import Form from "@/components/Home/Form.vue";
import Url from "@/components/Url/Url.vue";

export default {
  name: "home",

  components: {
    Form,
    Url
  },

  data() {
    return {
      response: null
    };
  },

  methods: {
    setUrl(payload) {
      this.response = payload;
    },

    loadResponseFromLocalStorage(){
        let response = {
            "longUrl": window.localStorage.getItem("longUrl"),
            "shortcode": window.localStorage.getItem("shortcode"),
        }

        this.response = response;
    }
  },

  mounted: function() {
    document.title = "clipit | Home";
    this.loadResponseFromLocalStorage();
  }
};
</script>
