<template>
  <div class="row text-left">
    <div class="col-12 col-md-6 mr-md-auto ml-md-auto">

      <div>
          
        <div>
          <h3>
            paste your long urls in the field below and have it 
            shortened. Or do you want to create custom urls?

            <span>
              <i 
                class="fa fa-arrow-right" 
                aria-hidden="true" 
                @click="hideForm"
              >
                custom
              </i>
            </span>

          </h3>
        </div>

        <form class="mt-5" @submit.prevent="onSubmit">
            <input
                class="form-control py-2 border-right-0 border"
                type="text"
                placeholder="paste your long url here"
                v-validate="'required|url'" 
                required
                name="url"
                v-model="longUrl"
            />

            <div class="mt-2">
                <span 
                    class="text-danger"
                >
                    {{ errors.first('url') }}
                </span>
            </div>

            <ClipButton :isLoading="isLoading"/>            
        </form>

      </div>
    </div>
  </div>
</template>

<script>
import ClipButton from "@/components/Utils/ClipButton.vue";

export default {
  name: "RegularForm",

  components: {
    ClipButton
  },

  props: {
      isLoading: {
          type: Boolean,
          required: true,
      }
  },

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

</style>
