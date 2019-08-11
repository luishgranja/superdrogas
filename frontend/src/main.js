import Vue from 'vue'
import App from './App.vue'
import admin from './router/admin'
import tenant from './router/tenant'
import store from './store'
import host from '@/utilities/host'
import TemplatePlugin from '@/template/TemplatePlugin'

Vue.use(TemplatePlugin)

Vue.config.productionTip = false

new Vue({
  router: host.isAdmin() ? admin : tenant,
  store,
  render: h => h(App)
}).$mount('#app')
