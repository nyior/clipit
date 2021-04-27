<template>
  <div class="row px-3">
    <div class="col-12 p-2 card shadow my-3 mx-2">
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

          <div class="col-2">
              <small id="copied" v-if="copied">
                <i class="fa fa-check-square-o" aria-hidden="true"></i>
              </small>
              <small v-else title="copy clipped url to clipboard">
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
                <tr>
                    <td>
                        <small>
                            <a
                                :href="scheme + host + encodeURI(this.url.shortcode)"
                                target="blank"
                            >
                                {{ host + url.shortcode  }}
                            </a>
                        </small>
                    </td>

                    <td>
                        <small>
                            <a :href="encodeURI(url.longUrl)" target="blank">
                                 {{ url.longUrl.substring(0, 15).concat('...') }}
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
        font-weight: bold;
    }
</style>

<script>
export default {
  name: 'url',

  props: {
    url: {
      type: Object,
      required: true
    }
  },

  data () {
    return {
      scheme: 'https://',
      copied: false,
      host: 'www.clipit.fun' + '/'
    }
  },

  methods: {
    setCopiedToFalse () {
      this.copied = false
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
  }
}
</script>
