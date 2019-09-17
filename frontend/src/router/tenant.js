import Vue from 'vue'
import Router from 'vue-router'
import store from '@/store'
import admin from './modules/admin'
import ecommerce from './modules/ecommerce'
import host from '@/utilities/host'
import Error404 from '@/components/errors/Error404'
import DoesNotExistTenant from '@/components/errors/DoesNotExistTenant'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    { ...admin },
    { ...ecommerce },
    {
      path: '/does-not-exist',
      name: 'does-not-exist',
      component: DoesNotExistTenant
    },
    {
      path: '*',
      component: Error404
    }
  ]
})

router.beforeEach((to, from, next) => {
  const tenantExist = store.getters['app/tenantExist']
  if (!tenantExist && to.path !== '/does-not-exist' && !host.isAdmin()) {
    next({ name: 'does-not-exist' })
  }

  const logged = store.getters['authentication/logged']
  switch (to.name) {
    case 'login':
      logged ? next({ name: 'home' }) : next()
      break
    case 'home':
    case 'users':
    case 'products':
    case 'batches':
    case 'brands':
    case 'categories':
      logged ? next() : next({ name: 'login' })
      break
    default:
      next()
  }
})

export default router
