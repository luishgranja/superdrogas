import http from '@/utilities/http'
import template from '@/utilities/template'

const state = {
  brands: [],
  brand: {},
  errors: {},
  isLoading: false
}

const getters = {
  isNewBrand: state => state.brand.id === undefined,
  activeBrands: state => {
    var brands = []
    state.brands.forEach(brand => {
      if (brand.is_active) {
        brands.push({
          id: brand.id,
          text: brand.name
        })
      }
    })
    return brands
  }

}

const mutations = {
  SET_BRANDS: (state, newBrands) => {
    state.brands = newBrands
  },
  SET_BRAND: (state, newBrand) => {
    state.brands = [
      ...state.brands.filter(brand => brand.id !== newBrand.id),
      newBrand
    ]
  },
  SET_ERRORS: (state, newErrors) => {
    state.errors = newErrors || {}
  },
  ADD_BRAND: (state, newBrand) => {
    state.brands.unshift(newBrand)
  },
  GET_BRAND: (state, brandId) => {
    state.brand = state.brands.find(brand => brand.id === brandId) || {}
  },
  SWITCH_BRAND_STATUS: state => {
    state.brands.forEach((brand, index) => {
      if (brand.id === state.brand.id) {
        state.brands[index].is_active = !state.brands[index].is_active
      }
    })
  },
  SET_LOAD_STATUS: (state, newLoadStatus) => {
    state.isLoading = newLoadStatus
  },
  SET_NAME: (state, newName) => {
    state.brand = { ...state.brand, name: newName }
  },
  SET_EMAIL: (state, newEmail) => {
    state.brand = { ...state.brand, email: newEmail }
  },
  SET_PHONE: (state, newPhone) => {
    state.brand = { ...state.brand, phone: newPhone }
  }
}

const actions = {
  getBrands: async ({ commit }) => {
    commit('SET_LOAD_STATUS', true)
    const response = await http.get('inventory/brands/')
    if (!response.error) {
      commit('SET_BRANDS', response.data)
    }
    commit('SET_LOAD_STATUS', false)
  },
  getBrand: ({ commit }, brandId) => {
    commit('SET_ERRORS')
    commit('GET_BRAND', brandId)
  },
  createBrand: async ({ state, commit }, event) => {
    if (event) event.preventDefault()
    commit('SET_ERRORS')
    const response = await http.post('inventory/brands/', state.brand)
    if (!response.error) {
      template.destroy()
      commit('ADD_BRAND', response.data)
      template.hideModal('#brand-form')
      commit('GET_BRAND')
    } else {
      commit('SET_ERRORS', response.data)
    }
  },
  updateBrand: async ({ state, commit }, event) => {
    if (event) event.preventDefault()
    commit('SET_ERRORS')
    const response = await http.patch(`inventory/brands/${state.brand.id}/`, state.brand)
    if (!response.error) {
      template.destroy()
      commit('SET_BRAND', response.data)
      template.hideModal('#brand-form')
    } else {
      commit('SET_ERRORS', response.data)
    }
  },
  deleteBrand: async ({ state, commit }) => {
    const response = await http.delete(`inventory/brands/${state.brand.id}/`)
    if (!response.error) {
      commit('SWITCH_BRAND_STATUS')
      template.hideModal('#brand-status')
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
