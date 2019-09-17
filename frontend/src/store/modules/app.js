import http from '@/utilities/http'
import host from '@/utilities/host'

const state = {
  isAdmin: host.isAdmin(),
  app: '',
  tenant: {}
}

const getters = {
  module: state => {
    switch (state.app) {
      case 'users':
      case 'customers':
        return 'accounts'
      case 'batches':
      case 'brands':
      case 'categories':
      case 'products':
        return 'inventory'
      default:
        return ''
    }
  },
  tenantExist: state => state.tenant.is_active || false
}

const mutations = {
  SET_APP: (state, newApp) => {
    state.app = newApp
  },
  SET_TENANT: (state, newTenant) => {
    state.tenant = newTenant
  }
}

const actions = {
  updateApp: ({ commit }, newApp) => {
    commit('SET_APP', newApp)
  },
  getTenantInformation: async ({ commit }) => {
    const response = await http.get(`tenant-info/${host.getSubdomain()}/`)
    commit('SET_TENANT', response.data)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
