<template>
  <div class="row px-5">
    <div class="col-12 col-md-6 ml-md-auto mr-md-auto p-2 card">
      <p id="url-stats">
        <router-link
          :to="{
            name: 'url-stats',
            params: { shortcode: url.shortcode }
          }"
        >
          view url stats
          <i class="fa fa-arrow-right" aria-hidden="true"> </i>
        </router-link>
      </p>
      <hr />

      <div>
        <small>
          original url:
          <a :href="encodeURI(url.longUrl)" target="blank">
            {{ url.longUrl.substring(0, 20).concat("...") }}
          </a>
        </small>
      </div>

      <div>
        <small>
          clipped url:
          <a :href="scheme + host + encodeURI(url.shortcode)" target="blank">
            {{ host + encodeURI(url.shortcode) }}
          </a>
        </small>
      </div>
    </div>
  </div>
</template>

<style scoped>
@media only screen and (max-width: 600px) {
}
</style>

<script>
export default {
  name: "url",

  props: {
    url: {
      type: Object,
      required: true
    }
  },

  data() {
    return {
      host: location.hostname + '/',
      scheme: location.protocol + '//'
    };
  },

  methods: {
    // setUrl(payload){
    //     this.response = payload;
    // }
  },

  mounted: function() {
    document.title = "Shortster | Home";
  }
};
</script>
