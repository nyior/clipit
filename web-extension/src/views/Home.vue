<template>
  <div class="container-fluid hero-container">

    <Form 
        @on-submit="setUrl" 
        @show-copied-to-clipboard-toaster="showCopiedToClipboardToaster"
        @invalid-url="showInvalidUrlToaster"
    />

    <div
        v-if="response !== null"
        class="row space-up text-left text-muted px-3"
    >
        <div class="col-12 text-center" v-if="showToaster">
              <h5 class="toaster">shortened URL copied to clipboard</h5>
        </div>
        
         <div class="col-12 text-center" v-if="isInvalidUrl">
              <h5 class="toaster">oops!!! this URL is invalid!</h5>
        </div>

        <div class="col-12">
            <div class="row text-left">
                <div class="col-12">
                    <h4>The most recent URL you worked with</h4>
                </div>
            </div>
            <Url :url="response" />
        </div>
    </div>

  </div>
</template>

<style scoped>
.toaster{
    background-color: #ff3855;
    color: white;
    font-weight: bold;
    padding: 0.5rem;
}
</style>

<script>
import Form from '@/components/Home/Form.vue'
import Url from '@/components/Utils/Url.vue'

export default {
  name: 'home',

  components: {
    Form,
    Url
  },

  data () {
    return {
      response: {
        longUrl: '',
        shortcode: ''
      },

      showToaster: false,
      isInvalidUrl: false
    }
  },

  methods: {
    setUrl (payload) {
      this.response = payload
    },

    setShowToasterToFalse () {
      this.showToaster = false
    },

    setIsInvalidUrlToFalse () {
      this.isInvalidUrl = false
    },

    showCopiedToClipboardToaster () {
      this.showToaster = true
      setTimeout(this.setShowToasterToFalse, 5000)
    },

    showInvalidUrlToaster () {
      this.isInvalidUrl = true
      setTimeout(this.setIsInvalidUrlToFalse, 3000)
    },

    loadResponseFromLocalStorage () {
      const response = {
        longUrl: window.localStorage.getItem('longUrl'),
        shortcode: window.localStorage.getItem('shortcode')
      }

      if (response.shortcode !== null) {
        this.response = response;
      }
    }
  },

  mounted: function () {
    this.loadResponseFromLocalStorage()
  }
}
</script>
