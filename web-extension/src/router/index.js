import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import UrlList from '@/views/UrlList.vue'
import UrlStats from '@/views/UrlStats.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },

  {
    path: '/urls-list',
    name: 'urls',
    component: UrlList
  },

  {
    path: '/url-stats',
    name: 'url-stats',
    component: UrlStats
  }
]

const router = new VueRouter({
  routes
})

export default router
