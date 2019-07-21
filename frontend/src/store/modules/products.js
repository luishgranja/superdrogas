import http from '@/utilities/http'
import template from '@/utilities/template'

const state = {
  products: [],
  product: {},
  errors: {},
  isLoading: false
}

const getters = {
  isNewProduct: state => state.product.id === undefined,
  activeProducts: state => state.products.filter(product => product.is_active)
}

const mutations = {
  SET_PRODUCTS: (state, newProducts) => {
    state.products = newProducts
  },

  SET_PRODUCT: (state, newProduct) => {
    state.products = [
      ...state.products.filter(product => product.id !== newProduct.id),
      newProduct
    ]
  },

  SET_ERRORS: (state, newErrors) => {
    state.errors = newErrors || {}
  },

  ADD_PRODUCT: (state, newProduct) => {
    state.products.unshift(newProduct)
  },

  GET_PRODUCT: (state, productId) => {
    state.product = state.products.find(product => product.id === productId) || {}
  },

  SWITCH_PRODUCT_STATUS: state => {
    state.products.forEach((product, index) => {
      if (product.id === state.product.id) {
        state.products[index].is_active = !state.products[index].is_active
      }
    })
  },

  SET_LOAD_STATUS: (state, newLoadStatus) => {
    state.isLoading = newLoadStatus
  },

  SET_NAME: (state, newName) => {
    state.product = { ...state.product, name: newName }
  },

  SET_DESCRIPTION: (state, newDescription) => {
    state.product = { ...state.product, description: newDescription }
  },

  SET_PRICE: (state, newPrice) => {
    state.product = { ...state.product, price: newPrice }
  },

  SET_IMAGE: (state, newImage) => {
    state.product = { ...state.product, image: newImage }
  },

  SET_CATEGORY: (state, newCategory) => {
    state.product = { ...state.product, category: newCategory }
  },

  SET_SKU: (state, newSku) => {
    state.product = { ...state.product, sku: newSku }
  },

  SET_WEIGHT: (state, newWeight) => {
    state.product = { ...state.product, weight: newWeight }
  },

  SET_BRAND: (state, newBrand) => {
    state.product = { ...state.product, brand: newBrand }
  }
}

const actions = {
  getProducts: async ({ commit }) => {
    commit('SET_LOAD_STATUS', true)
    const response = await http.get('products/')
    if (!response.error) {
      commit('SET_PRODUCTS', response.data)
    }
    commit('SET_LOAD_STATUS', false)
  },
  getProduct: ({ commit }, productId) => {
    commit('SET_ERRORS')
    commit('GET_PRODUCT', productId)
  },

  createProduct: async ({ state, commit }, event) => {
    if (event) event.preventDefault()
    commit('SET_ERRORS')
    const response = await http.post('products/', state.product)
    if (!response.error) {
      commit('ADD_PRODUCT', response.data)
      template.hideModal('#product-form')
      commit('GET_PRODUCT')
    } else {
      commit('SET_ERRORS', response.data)
    }
  },

  updateProduct: async ({ state, commit }, event) => {
    if (event) event.preventDefault()
    commit('SET_ERRORS')
    const response = await http.patch(`products/${state.product.id}/`, state.product)
    if (!response.error) {
      commit('SET_product', response.data)
      template.hideModal('#product-form')
    } else {
      commit('SET_ERRORS', response.data)
    }
  },

  deleteProduct: async ({ state, commit }) => {
    const response = await http.delete(`products/${state.product.id}/`)
    if (!response.error) {
      commit('SWITCH_PRODUCT_STATUS')
      template.hideModal('#product-status')
    }
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
