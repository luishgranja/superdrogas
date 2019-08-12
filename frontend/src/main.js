import Vue from 'vue'
import VeeValidate from 'vee-validate'
import App from './App.vue'
import admin from './router/admin'
import tenant from './router/tenant'
import store from './store'
import host from '@/utilities/host'
import TemplatePlugin from '@/template/TemplatePlugin'

Vue.use(VeeValidate, { errorBagName: 'veeErrors' })
Vue.use(TemplatePlugin)

Vue.config.productionTip = false

const router = host.isAdmin() ? admin : tenant

router.afterEach((to, from) => {
  if (to.name === 'home' && from.name === 'login') {
    location.href = to.path
  }
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
