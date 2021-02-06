<template>
  <div class="container-fluid hero-container">
      <Form />
  </div>
</template>

<style scoped>
@media only screen and (max-width: 600px) {
	
}
</style>

<script>
import Form from "@/components/Home/Form.vue";

export default {
  name: "home",

  components: {
    Form
  },

  methods: {
    
  },

  mounted: function() {
    document.title = "Shortster | Home";
  }
};
</script>
