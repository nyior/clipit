<template>
  <div class="row px-3">
    <div class="col-12 p-2 card my-2 mx-2">
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
                <tr>
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
                                {{ url.longUrl.substring(0, 10).concat("...") }}
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
  name: 'url',

  props: {
    url: {
      type: Object,
      required: true
    }
  },

  data () {
    return {
      host: 'www.clipit.fun' + '/',
      scheme: 'https://'
    }
  },

  mounted: function () {
    document.title = 'Shortster | Home'
  }
}
</script>
