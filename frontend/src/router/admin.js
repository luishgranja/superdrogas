import Vue from 'vue'
import Router from 'vue-router'
import store from '@/store'
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

router.beforeEach((to, from, next) => {
  const logged = store.getters['authentication/logged']
  switch (to.name) {
    case 'login':
      logged ? next({ name: 'home' }) : next()
      break
    case 'home':
    case 'users':
      logged ? next() : next({ name: 'login' })
      break
    case 'products':
    case 'batches':
      break
    default:
      next()
  }
})

export default router
