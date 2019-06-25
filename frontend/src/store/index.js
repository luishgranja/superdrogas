import Vue from 'vue'
import Vuex from 'vuex'
import VuexI18n from 'vuex-i18n'
import app from './modules/app'

import * as getters from './getters'

Vue.use(Vuex)

const store = new Vuex.Store({
  strict: true,
  getters,
  modules: {
    app,
  },
  state: {},
  mutations: {}
})

Vue.use(VuexI18n.plugin, store)

export default store
