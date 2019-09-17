// import http from '@/utilities/http'
import admin from '@/router/admin'
import tenant from '@/router/tenant'
import host from '@/utilities/host'
import template from '@/utilities/template'

const router = host.isAdmin() ? admin : tenant

const state = {
  cartProducts: [],
  saleInvoice: {},
  productsInvoice: [],
  formData: new FormData()
}

const getters = {
  itemsOnCart: state => (state.cartProducts) ? state.cartProducts.length : 0,
  isCartEmpty: state => (state.cartProducts) ? state.cartProducts.length === 0 : false,
  total: (state) => {
    var total = 0
    for (let i = 0; i < state.cartProducts.length; i++) {
      total += state.cartProducts[i].quantity * state.cartProducts[i].price
    }
    return total
  }
}

const mutations = {
  ADD_TO_CART: (state, newProduct) => {
    let product = state.cartProducts.find(product => product.id === newProduct.id)
    if (!product) {
      state.cartProducts.push({ ...newProduct, quantity: 1 })
    } else {
      state.cartProducts = [
        ...state.cartProducts.filter(product => product.id !== newProduct.id),
        { ...product, quantity: product.quantity + 1 }
      ]
    }
  },
  DELETE_FROM_CART: (state, newProduct) => {
    newProduct.quantity--
    if (newProduct.quantity === 0) {
      state.cartProducts = [
        ...state.cartProducts.filter(product => product.id !== newProduct.id)
      ]
    } else {
      state.cartProducts = [
        ...state.cartProducts.filter(product => product.id !== newProduct.id),
        newProduct
      ]
    }
  },
  SET_SALE_INVOICE: (state, newSaleInvoice) => {
    state.saleInvoice = newSaleInvoice
  },
  ADD_PRODUCT_INVOICE: (state, newProductInvoice) => {
    state.productsInvoice.unshift(newProductInvoice)
  },
  BUILD_REQUEST (state, getters) {
    state.formData.append('user_id', '1')
    state.formData.append('client_id', '1')
    state.formData.append('sale_type', 'online')
    state.formData.append('total_amount', getters.pagoTotal)
  },
  BUILD_REQUEST_PRODUCTS (state, { getters, i, saleId }) {
    state.formData.append('sale_invoice_id', saleId)
    state.formData.append('product_id', getters.cartProducts[i].id)
    state.formData.append('quantity', getters.cartProducts[i].quantity)
    state.formData.append('total_price', getters.cartProducts[i].price)
    state.formData.append('is_active', true)
  }
}

const actions = {
  addToCart: ({ commit }, product) => {
    commit('ADD_TO_CART', product)
  },
  deleteFromCart: ({ commit }, product) => {
    template.destroy()
    commit('DELETE_FROM_CART', product)
  },
  checkout: async ({ state, commit, getters }, event) => {
    if (event) event.preventDefault()
    // commit('BUILD_REQUEST', getters)
    // const response = await http.post('sales/sales_invoice/', state.formData)
    // const saleId = response.data.id
    // if (!response.error) {
    //   commit('SET_SALE', response.data)
    //   for (var i = 0; i < getters.cartProducts.length; i++) {
    //     commit('BUILD_REQUEST_PRODUCTS', { getters, i, saleId })
    //     var responseProduct = await http.post('sales/product_on_sale/', state.formData)
    //     if (!responseProduct.error) {
    //       commit('ADD_PRODUCT_SALE', responseProduct.data)
    //     }
    //   }
    router.push({ name: 'checkout' })
    // }
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
