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
  },
  downloadData: async (context) => {
    const response = await http.get(`accounts/tenant_backup?schema_name=${host.getSubdomain()}`)
    var data = 'data:text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(response.data))
    var download = document.getElementById('download')
    download.setAttribute('href', data)
    download.setAttribute('download', 'data.json')
    download.click()
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
