import host from '@/utilities/host'

const state = {
  isAdmin: host.isAdmin(),
  app: ''
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
  }
}

const mutations = {
  SET_APP: (state, newApp) => {
    state.app = newApp
  }
}

const actions = {
  updateApp: ({ commit }, newApp) => {
    commit('SET_APP', newApp)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
