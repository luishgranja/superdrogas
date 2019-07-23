import Vue from 'vue'
import store from '@/store'
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

router.beforeEach((to, from, next) => {
  const logged = store.getters['authentication/logged']
  switch (to.name) {
    case 'login':
      logged ? next({ name: 'home' }) : next()
      break
    case 'home':
    case 'users':
    case 'products':
    case 'batches':
      logged ? next() : next({ name: 'login' })
      break
    default:
      next()
  }
})

export default router
