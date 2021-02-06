import Vue from "vue";
import Router from "vue-router";
import Home from "@/views/Home/Home.vue";
import UrlStats from "@/views/Url/UrlStats.vue";
import UrlList from "@/views/Url/UrlList.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },

    {
      path: "/url-stats/:shortcode",
      name: "url-stats",
      props: true,
      component: UrlStats
    },

    {
      path: "/url-list",
      name: "url-list",
      component: UrlList
    }
  ]
});
