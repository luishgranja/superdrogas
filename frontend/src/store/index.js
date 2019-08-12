import Vue from 'vue'
import Vuex from 'vuex'
import app from './modules/app'
import authentication from './modules/authentication'
import users from './modules/users'
import batches from './modules/batches'
import products from './modules/products'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    app,
    authentication,
    users,
    batches,
    products
  }
})
