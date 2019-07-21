import Vue from 'vue'
import Vuex from 'vuex'
import users from './modules/users'
import batches from './modules/batches'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    users,
    batches
  }
})
