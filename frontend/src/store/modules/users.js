import http from '@/utilities/http'

const state = {
  users: {},
  isLoading: false
}

const mutations = {
  SET_USERS: (state, newUsers) => {
    state.users = newUsers
  },
  SET_LOAD_STATUS: (state, newLoadStatus) => {
    state.isLoading = newLoadStatus
  }
}

const actions = {
  getUsers: async ({ commit }) => {
    commit('SET_LOAD_STATUS', true)
    const data = await http.get('users')
    if (data.status == null) {
      commit('SET_USERS', data)
    }
    commit('SET_LOAD_STATUS', false)
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
