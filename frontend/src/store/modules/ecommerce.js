import http from '@/utilities/http'
import router from '@/router'
import store from '@/store'

const state = {
  added: []
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
  DELETE_FROM_CART: (state, { id }) => {    
    var record = state.added.find(p => p.id === id)
    if (record.quantity == 1) {
      state.added = [
      ...state.added.filter(p => p.id !== id)
      ]
    } else {
      record.quantity--
    }
  }
}

// actions
const actions = {
  addToCart: ({ commit }, product) => {
    commit('ADD_TO_CART', {
      id: product.id
    })
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
