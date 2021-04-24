import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import UrlStats from '@/views/Url/UrlStats.vue'
import UrlList from '@/views/Url/UrlList.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },

  {
    path: '/url-stats/:shortcode',
    name: 'url-stats',
    props: true,
    component: UrlStats
  },

  {
    path: '/url-list',
    name: 'url-list',
    component: UrlList
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
