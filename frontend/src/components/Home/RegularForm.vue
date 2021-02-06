<template>
  <div class="row text-left">
    <div class="col-12 col-md-6 mr-md-auto ml-md-auto">
      <div>
        <div>
          <h3>
            paste your long urls in the field below and have it shortened. Or do
            you want to create custom urls?
            <span>
              <i class="fa fa-arrow-right" aria-hidden="true" @click="hideForm">
                custom
              </i>
            </span>
          </h3>
        </div>

        <form class="input-group mt-5" @submit.prevent="onSubmit">
          <input
            class="form-control py-2 border-right-0 border"
            type="text"
            placeholder="paste your long url here"
            v-model="longUrl"
          />
          <span class="input-group-append">
            <div class="input-group-text bg-white">
              <i class="fa fa-scissors" aria-hidden="true" @click="onSubmit">
              </i>
            </div>
          </span>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "RegularForm",

  data() {
    return {
      longUrl: null
    };
  },

  methods: {
    hideForm() {
      this.$emit("hide-form");
    },

    onSubmit() {
      this.$emit("on-submit", { longUrl: this.longUrl });
    }
  }
};
</script>

<style scoped>
.fa-scissors {
  color: #007f37;
  font-weight: bold !important;
  font-size: 3rem;
}
</style>
