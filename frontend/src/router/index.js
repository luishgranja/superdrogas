import Vue from 'vue'
import Router from 'vue-router'
import home from './modules/home'
import landing from './modules/landing'
import authorization from './modules/authorization'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    { ...home },
    { ...landing },
    { ...authorization }
  ]
})

export default router
