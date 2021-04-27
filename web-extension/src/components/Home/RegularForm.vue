<template>
  <div class="row text-left">
    <div class="col-12 col-md-6 mr-md-auto ml-md-auto">
        <div>
          <h3>
            Do you want to create custom URLs? we've got you!

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
                class="form-control py-2 my-3 border-right-0 border long-url-input"
                type="text"
                placeholder="paste your long url here"
                required
                name="url"
                v-model="longUrl"
            />

            <ClipButton :isLoading="isLoading"/>
        </form>
    </div>
  </div>
</template>

<script>
import { store } from '@/store.js'
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
    },

    tabUrl: {
      type: String,
      required: true
    }
  },

  data () {
    return {
      longUrl: store.state.tabUrl
    }
  },

  methods: {
    hideForm () {
      this.$emit('hide-regular-form')
    },

    onSubmit () {
      this.$emit('on-submit', { longUrl: this.longUrl })
    }
  }
}
</script>

<style scoped>

</style>
