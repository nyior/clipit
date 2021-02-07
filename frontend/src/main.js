import Vue from "vue";
import VeeValidate from 'vee-validate';

import App from "./App.vue";
import router from "./router/router";

Vue.config.productionTip = false;
Vue.use(VeeValidate);

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
