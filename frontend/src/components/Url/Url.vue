<template>
  <div class="row px-5">
    <div class="col-12 col-md-6 ml-md-auto mr-md-auto shadow p-4 card my-4">
      <div class="row">
          <div class="col-10 mr-auto">
            <router-link
                :to="{
                    name: 'url-stats',
                    params: { shortcode: url.shortcode }
                }"
            >
                <small>
                    <i class="fa fa-info-circle" aria-hidden="true"></i>
                    url stats
                </small>
            </router-link>
          </div>

          <div class="col-2 ml-auto">
              <small>
                <i class="fa fa-clone" aria-hidden="true"></i>
              </small>
          </div>
      </div>
        
      <hr />

      <table class="table borderless table-sm">
            <thead>
                <tr 
                    class="text-left"
                >
                    <th>clipped</th>
                    <th>original</th>
                </tr>
            </thead>

            <tbody>
                <tr class="p-2">
                    <td>
                        <small>
                            <a :href="scheme + host + encodeURI(url.shortcode)" target="blank">
                                    {{ host + encodeURI(url.shortcode) }}
                            </a>
                        </small>
                    </td> 

                    <td>
                        <small>
                            <a :href="encodeURI(url.longUrl)" target="blank">
                                {{ url.longUrl.substring(0, 20).concat("...") }}
                            </a>
                        </small>
                    </td>      
                </tr>        
            </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>

a{
    color: #293a48 !important;
}
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
      host: window.location.hostname + '/',
      scheme: 'https://'
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
