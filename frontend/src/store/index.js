import Vue from 'vue'
import Vuex from 'vuex'
import app from './modules/app'
import authentication from './modules/authentication'
import users from './modules/users'
import batches from './modules/batches'
import brands from './modules/brands'
import categories from './modules/categories'
import products from './modules/products'
import tenants from './modules/tenants'
import ecommerce from './modules/ecommerce'
import sales from './modules/sales'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    app,
    authentication,
    users,
    batches,
    brands,
    categories,
    products,
    tenants,
    ecommerce,
    sales
  }
})
