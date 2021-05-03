import Vue from 'vue'

import Popup from './Popup.vue'
import router from '@/router/index'

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(Popup)
}).$mount('#app')
