import Vue from 'vue'
import Router from 'vue-router'
import home from './modules/home'
import landing from './modules/landing'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    { ...home },
    { ...landing }
  ]
})

export default router
