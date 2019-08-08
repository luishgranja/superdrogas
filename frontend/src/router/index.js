import Vue from 'vue'
import Router from 'vue-router'
import admin from './modules/admin'
import ecommerce from './modules/ecommerce'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    { ...admin },
    { ...ecommerce }
  ]
})

export default router
