<template>
  <div class="container-fluid hero-container">
    <Form @on-submit="setUrl" />

    <div 
        class="space-up" 
        v-if="response !== null"
    >
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
    }
  },

  mounted: function() {
    document.title = "clipit | Home";
  }
};
</script>
