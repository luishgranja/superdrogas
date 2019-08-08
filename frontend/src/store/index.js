import Vue from 'vue'
import Vuex from 'vuex'

// Application state
import authentication from './modules/authentication'

// Accounts module
import users from './modules/users'

// Inventory module
import batches from './modules/batches'
import products from './modules/products'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    users,
    batches,
    products,
    authentication
  }
})
