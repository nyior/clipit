<template>
  <div class="row px-5 text-center">
    <div class="col-12 col-md-6 ml-md-auto mr-md-auto p-2 error">
        <p>{{ errorMessage }}</p>
    </div>
  </div>
</template>

<style scoped>
.error{
    background-color: #ff3855;
    color: white;
    font-weight: bolder;
}
</style>

<script>
export default {
  name: "Error",

  props: {
    errorMessage: {
      type: String,
      required: true
    }
  }
};
</script>
