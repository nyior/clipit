import Vue from 'vue'
import Popup from './Popup.vue'
import router from '@/router/index'

/* eslint-disable no-new */
new Vue({
  router,
  el: '#app',
  render: h => h(Popup)
})
