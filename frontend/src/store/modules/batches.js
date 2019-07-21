import http from '@/utilities/http'
import template from '@/utilities/template'

const state = {
  batches: [],
  batch: {},
  errors: {},
  isLoading: false
}

const getters = {
  isNewBatch: state => state.batch.id === undefined
}

const mutations = {
  SET_BATCHES: (state, newBatches) => {
    state.batches = newBatches
  },
  SET_BATCH: (state, newBatch) => {
    state.batches = [
      ...state.batches.filter(batch => batch.id !== newBatch.id),
      newBatch
    ]
  },
  SET_ERRORS: (state, newErrors) => {
    state.errors = newErrors || {}
  },
  ADD_BATCH: (state, newBatch) => {
    state.batches.unshift(newBatch)
  },
  GET_BATCH: (state, batchId) => {
    state.batch = state.batches.find(batch => batch.id === batchId) || {}
  },
  SWITCH_BATCH_STATUS: state => {
    state.batches.forEach((batch, index) => {
      if (batch.id === state.batch.id) {
        state.batches[index].is_active = !state.batches[index].is_active
      }
    })
  },
  SET_LOAD_STATUS: (state, newLoadStatus) => {
    state.isLoading = newLoadStatus
  },
  SET_PRODUCT: (state, newProduct) => {
    state.batch = { ...state.batch, product: newProduct }
    console.log("me cago en todo")
  },
  SET_QUANTITY: (state, newQuantity) => {
    state.batch = { ...state.batch, quantity: newQuantity }
  },
  SET_MANUFACTURING_DATE: (state, newManufacturingDate) => {
    state.batch = { ...state.batch, manufacturing_date: newManufacturingDate }
  },
  SET_EXPIRATION_DATE: (state, newExpirationDate) => {
    state.batch = { ...state.batch, expiration_date: newExpirationDate }
  }
}

const actions = {
  getBatches: async ({ commit }) => {
    commit('SET_LOAD_STATUS', true)
    const response = await http.get('batches/')
    if (!response.error) {
      commit('SET_BATCHES', response.data)
    }
    commit('SET_LOAD_STATUS', false)
  },
  getBatch: ({ commit }, batchId) => {
    commit('SET_ERRORS')
    commit('GET_BATCH', batchId)
  },
  createBatch: async ({ state, commit }, event) => {
    if (event) event.preventDefault()
    commit('SET_ERRORS')
    const response = await http.post('batches/', state.batch)
    if (!response.error) {
      commit('ADD_BATCH', response.data)
      template.hideModal('#batch-form')
      commit('GET_BATCH')
    } else {
      commit('SET_ERRORS', response.data)
    }
  },
  updateBatch: async ({ state, commit }, event) => {
    if (event) event.preventDefault()
    commit('SET_ERRORS')
    const response = await http.patch(`batches/${state.batch.id}/`, state.batch)
    if (!response.error) {
      commit('SET_BATCH', response.data)
      template.hideModal('#batch-form')
    } else {
      commit('SET_ERRORS', response.data)
    }
  },
  deleteBatch: async ({ state, commit }) => {
    const response = await http.delete(`batches/${state.batch.id}/`)
    if (!response.error) {
      commit('SWITCH_BATCH_STATUS')
      template.hideModal('#batch-status')
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
