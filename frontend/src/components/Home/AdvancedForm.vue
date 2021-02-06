<template>
  <div class="row text-left">
    <div class="col-12 col-md-6 ml-md-auto mr-md-auto">
      <div>
        <div>
          <h3>
            you don't want to create custom urls? we've got you!
            <span>
              <i class="fa fa-arrow-left" aria-hidden="true" @click="hideForm">
                back
              </i>
            </span>
          </h3>
        </div>

        <form class="mt-5" @submit.prevent="onSubmit">
          <input
            class="form-control py-2 my-2"
            type="text"
            placeholder="paste your long url here"
            v-model="longUrl"
            required
          />

          <input
            class="form-control py-2 my-2"
            type="text"
            placeholder="custom url(between 4 - 30 characters)"
            v-model="shortcode"
            required
          />

          <button type="submit" class="btn py-2 my-2">
            submit
          </button>
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
      longUrl: null,
      shortcode: null
    };
  },

  methods: {
    hideForm() {
      this.$emit("hide-form");
    },

    onSubmit() {
      this.$emit("on-submit", {
        longUrl: this.longUrl,
        shortcode: this.shortcode
      });
    }
  }
};
</script>

<style scoped></style>
