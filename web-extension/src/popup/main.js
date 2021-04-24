import { createApp } from 'vue'
import Popup from './Popup.vue'
import router from '@/router/index'

createApp(Popup)
  .use(router)
  .mount('#app')
