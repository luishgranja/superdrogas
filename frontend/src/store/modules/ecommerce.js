import http from '@/utilities/http'
import router from '@/router'

const state = {
  added: [],
  products: [
    {
      id: 'cc919e21-ae5b-5e1f-d023-c40ee669520c',
      name: 'COBOL 101 vintage',
      description: 'Learn COBOL with this vintage programming book',
      price: 399
    },
    {
      id: 'bcd755a6-9a19-94e1-0a5d-426c0303454f',
      name: 'Sharp C2719 curved TV',
      description: 'Watch TV like never before with the brand new curved screen technology',
      price: 1995
    },
    {
      id: '727026b7-7f2f-c5a0-ace9-cc227e686b8e',
      name: 'Remmington X mechanical keyboard',
      description: 'Excellent for gaming and typing, this Remmington X keyboard ' +
        'features tactile, clicky switches for speed and accuracy',
      price: 595
    }
  ]
}

// getters
const getters = {
  allProducts: state => state.products, // would need action/mutation if data fetched async
  getNumberOfProducts: state => (state.products) ? state.products.length : 0,
  itemsOnCart: state => (state.added) ? state.added.length : 0,
  cartProducts: state => {
    return state.added.map(({ id, quantity }) => {
      const product = state.products.find(p => p.id === id)
      return {
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
  }
}

// actions
const actions = {
  addToCart: ({ commit }, product) => {
    commit('ADD_TO_CART', {
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
