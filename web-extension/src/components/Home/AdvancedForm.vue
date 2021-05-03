<template>
  <div class="row text-left">
    <div class="col-12 col-md-6 ml-md-auto mr-md-auto">
      <div>
        <div>
          <h3>
            you don't want to create custom URLs? we've got you!
            <span>
              <i
                class="fa fa-arrow-left"
                aria-hidden="true"
                @click="hideForm"
              >
                back
              </i>
            </span>
          </h3>
        </div>

        <form class="mt-5" @submit.prevent="onSubmit">
          <input
            class="form-control py-2 my-3 long-url-input"
            type="text"
            placeholder="paste your long url here"
            name="url"
            v-model="longUrl"
            required
          />

          <input
            class="form-control py-2 my-3"
            type="text"
            placeholder="custom url(between 4 - 30 characters)"
            name="shortcode"
            v-model="shortcode"
            required
          />

          <ClipButton :isLoading="isLoading"/>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import ClipButton from '@/components/Utils/ClipButton.vue'

export default {
  name: 'RegularForm',

  components: {
    ClipButton
  },

  props: {
    isLoading: {
      type: Boolean,
      required: true
    }
  },

  data () {
    return {
      longUrl: null,
      shortcode: null
    }
  },

  methods: {
    hideForm () {
      this.$emit('show-regular-form')
    },

    onSubmit () {
      this.$emit('on-submit', {
        longUrl: this.longUrl,
        shortcode: this.shortcode
      })
    }
  },

  beforeMount: function () {
    this.longUrl = window.localStorage.getItem('tabUrl')
  }
}
</script>

<style scoped>
small{
    font-weight: bold;
}
</style>
