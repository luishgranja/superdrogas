import http from '@/utilities/http'
import router from '@/router'
import store from '@/store'

const state = {
  added: [],
  formData: new FormData(),
  sale_invoice: {},
  products_invoice: []
}

// getters
const getters = {      
  itemsOnCart: state => (state.added) ? state.added.length : 0,
  emptyCart: state => (state.added) ? state.added.length == 0: false,
  cartProducts: state => {
    var products = store.state.products.products 
    return state.added.map(({ id, quantity }) => {
      const product = products.find(p => p.id === id)
      return {
        id: product.id,
        name: product.name,
        price: product.price,
        quantity
      }
    })
  },
  pagoTotal: (state, getters) => {    
    var total = 0
    for (var i = 0; i < getters.cartProducts.length; i++){
      total += getters.cartProducts[i].quantity *  getters.cartProducts[i].price
    }
    return total
  },
  noIva: (state, getters) => {    
    var noIva = 0
    const total = getters.pagoTotal 
    noIva = total - total * 0.19
    return noIva
  },
  iva: (state, getters) => {    
    var iva = 0
    const total = getters.pagoTotal 
    iva = total * 0.19
    return iva
  }


}

// mutations
const mutations = {
  ADD_TO_CART: (state, { id }) => {    
    const record = state.added.find(p => p.id === id)
    if (!record) {
      state.added.push({
        id,
        quantity: 1
      })
    } else {
      record.quantity++
    }     
  },
  ADD_PRODUCT_SALE: (state, newProduct) => {
    state.products_invoice.unshift(newProduct)
  },
  DELETE_FROM_CART: (state, { id }) => {    
    var record = state.added.find(p => p.id === id)
    if (record.quantity == 1) {
      state.added = [
      ...state.added.filter(p => p.id !== id)
      ]
    } else {
      record.quantity--
    }
  },
  BUILD_REQUEST (state, getters) {
    state.formData.append('user_id', "1")
    state.formData.append('client_id', "1")
    state.formData.append('sale_type', "online")    
    state.formData.append('total_amount', getters.pagoTotal)    
  },
  BUILD_REQUEST_PRODUCTS (state, { getters, i, saleId }) {    
    state.formData.append('sale_invoice_id', saleId)
    state.formData.append('product_id', getters.cartProducts[i].id)
    state.formData.append('quantity', getters.cartProducts[i].quantity)    
    state.formData.append('total_price', getters.cartProducts[i].price)
    state.formData.append('is_active', true)    
  },
  SET_SALE: (state, newSale) => {
    state.sale_invoice = newSale
  }
}
// actions
const actions = {
  addToCart: ({ commit }, product) => {
    commit('ADD_TO_CART', {
      id: product.id
    })
  },
  checkout: async ({ state, commit, getters }, event) => {
    if (event) event.preventDefault()
    //commit('SET_ERRORS')
    commit('BUILD_REQUEST', getters)    
    const response = await http.post('sales/sales_invoice/', state.formData)
    const saleId = response.data.id
    if (!response.error) {
      commit('SET_SALE', response.data)
      for (var i = 0; i < getters.cartProducts.length; i++){        
        commit('BUILD_REQUEST_PRODUCTS', { getters, i, saleId })
        var response_product = await http.post('sales/product_on_sale/', state.formData)
        if(!response_product.error) {
          commit('ADD_PRODUCT_SALE', response_product.data)
        }
      }      
      router.push({ name: 'checkout' })
      //commit('GET_PRODUCT')
    } else {
      //commit('SET_ERRORS', response.data)
    }
  },
  deleteFromCart: ({ commit }, product) => {
    commit('DELETE_FROM_CART', {
      id: product.id
    })
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
