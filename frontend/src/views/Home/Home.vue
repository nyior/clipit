<template>
  <div class="container-fluid hero-container">
    
    <Form 
        @on-submit="setUrl" 
        @show-copied-to-clipboard-toaster="showCopiedToClipboardToaster"
    />

    <div 
        class="space-up" 
        v-if="response !== null"
    >
      <div class="row text-center px-5" v-if="showToaster">
          <div class="col-12 col-md-6 mr-md-auto ml-md-auto text-center">
              <h5 class="toaster">shortened URL copied to clipboard</h5>
          </div>
      </div>

      <div class="row text-left text-muted px-5">
          <div class="col-12 col-md-6 mr-md-auto ml-md-auto">
              <h4>The most recent URL you worked with</h4>
          </div>
      </div>

      <div class="row text-left text-muted px-md-5 px-3">
          <div class="col-12">
              <Url :url="response" />
          </div>
      </div>
    </div>

    <div class="space-up">
        <div class="row text-left px-5">
            <div class="col-12 col-md-6 mr-md-auto ml-md-auto">
                <h4>Want to install our browser extension?</h4>
            </div>
        </div>

        <div class="row text-center mt-2 px-5">
            <div class="col-12 col-md-6 mr-md-auto ml-md-auto text-left">
                <a href="" class="btn mr-2 shadow">
                   <i class="fa fa-chrome" aria-hidden="true">
                       chrome
                   </i>
                </a>

                <a href="" class="btn shadow">
                   <i class="fa fa-firefox" aria-hidden="true">
                       firefox
                   </i>
                </a>
            </div>
        </div>

        <div class="row text-left mt-4 px-5">
            <div class="col-12 col-md-6 mr-md-auto ml-md-auto">
                <p>
                    Our browser extension makes the URL shortening process 
                    more convenient. How does it work?

                </p>
            </div>
        </div>

        <div class="row h-100 text-center mt-2 px-5">
            <div class="col-12 col-md-6 mr-md-auto ml-md-auto text-left">
                <iframe 
                    src="https://www.youtube.com/embed/GzSVSA-EO74" 
                    title="how clipit browser extensions work"
                    class="card shadow"
                >

                </iframe>
            </div>
        </div>
    </div>
  </div>
</template>

<style scoped>
iframe{
    height: 350px;
    width: 100%;
    border: none;
    padding: 1rem;
}

.toaster{
    background-color: #ff3855;
    color: white;
    font-weight: bold;
    padding: 0.5rem;
}
@media only screen and (max-width: 600px) {
  iframe{
    height: 200px;
}
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
      response: { 
        "longUrl": '',
        "shortcode": '',
      },

      showToaster: false,
    };
  },

  methods: {
    setUrl (payload) {
      this.response = payload;
    },

    setShowToasterToFalse () {
      this.showToaster = false
    },

    showCopiedToClipboardToaster () {
      this.showToaster = true
      setTimeout(this.setShowToasterToFalse, 3000)
    },

    loadResponseFromLocalStorage () {
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
