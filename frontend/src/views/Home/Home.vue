<template>
  <div class="container-fluid hero-container">
    
    <Form @on-submit="setUrl" />

    <div 
        class="space-up" 
        v-if="response !== null"
    >
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

    <div class="row text-center px-5 space-up">
        <div class="col-12 col-md-6 mr-md-auto ml-md-auto">
            <h3
                class="animate"
            >
               <span class="mr-2">30</span>active users and still couting ...
            </h3>
        </div>
    </div>

    <div class="space-up">
        <div class="row text-left px-md-0 px-4">
            <div class="col-12 col-md-6 mr-md-auto ml-md-auto">
                <h4>How do our browser extensions work?</h4>
            </div>
        </div>

        <div class="row h-100 text-center mt-2 px-5">
            <div class="col-12 card shadow col-md-6 mr-md-auto ml-md-auto text-left">
                <iframe 
                    src="https://www.youtube.com/embed/GzSVSA-EO74" 
                    title="how clipit browser extensions work"
                >

                </iframe>
            </div>
        </div>

        <div class="row h-100 text-center mt-4 px-md-0 px-4">
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
    </div>
  </div>
</template>

<style scoped>
iframe{
    height: 350px;
    width: 100%;
    border: none;
}
.animate {
  animation-name: animate-animation;
  animation-duration: 2.5s;
  animation-iteration-count: infinite;
  font-weight: bold;
}

@keyframes animate-animation {
  from {
    font-size: 0.8rem;
  }
  to {
    font-size: 1.4rem;
  }
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
      response: null
    };
  },

  methods: {
    setUrl(payload) {
      this.response = payload;
    },

    loadResponseFromLocalStorage(){
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
