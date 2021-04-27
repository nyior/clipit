<template>
  <div class="row px-5">
    <div class="col-12 col-md-6 ml-md-auto mr-md-auto shadow p-2 card my-4">
      <div class="row">
          <div class="col-10 mr-auto">
            <router-link
                :to="{
                    name: 'url-stats',
                    params: { shortcode: url.shortcode }
                }"
            >
                <small title="see how users are interacting with this URL">
                    <i class="fa fa-info-circle" aria-hidden="true"> url stats</i>
                </small>
            </router-link>
          </div>

          <div class="col-2 text-md-right text-left">
              <small id="copied" v-if="copied">
                <i class="fa fa-check-square-o" aria-hidden="true"></i>
              </small>
              <small v-else title="copy to clipboard">
                <i 
                    class="fa fa-clone" 
                    aria-hidden="true"
                    @click="copyToClipboard"
                >
                </i>
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
                            <a 
                                id="clipped-url" 
                                :href="scheme + host + encodeURI(this.url.shortcode)" 
                                target="blank"
                            >
                                {{ host + url.shortcode }}
                            </a>
                        </small>
                    </td> 

                    <td>
                        <small>
                            <a 
                                :href="encodeURI(url.longUrl)" 
                                target="blank"
                                :title="url.longUrl"
                            >
                                {{ url.longUrl.substring(0, 15).concat("...") }}
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

#copied{
   color: #01af5e;
   font-weight: bolder;
   font-size: 2rem;
}
@media only screen and (max-width: 600px) {
}
</style>

<script>
import { host, copiedToClipboard } from "@/utils/helper.js";
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
      scheme: 'https://',
      copied: false,
      host: host
    };
  },

  methods: {
    setCopiedToFalse () {
        this.copied = false;
    },

    copyToClipboard () {
      try {
        const clippedUrl = this.host + encodeURI(this.url.shortcode)
        navigator.clipboard.writeText(clippedUrl)
        this.copied = true

        setTimeout(this.setCopiedToFalse, 2000)
      } catch (err) {
        this.copied = false
      }
    }
  },

  mounted: function() {
    document.title = "Shortster | Home";
  }
};
</script>
