import Vue from 'vue'
import Router from 'vue-router'
import admin from './modules/admin'
import landing from './modules/landing'
import Error404 from '@/components/errors/Error404'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    { ...admin },
    { ...landing },
    {
      path: '*',
      component: Error404
    }
  ]
})

export default router
