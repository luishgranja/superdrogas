import http from '@/utilities/http'
import template from '@/utilities/template'

const state = {
  userList: [],
  currentUser: {},
  isLoading: false
}

const mutations = {
  SET_USER_LIST: (state, newUserList) => {
    state.userList = newUserList
  },
  GET_USER: (state, userId) => {
    state.currentUser = state.userList.find(user => user.id === userId) || {}
  },
  SWITCH_USER_STATUS: state => {
    state.userList.forEach((user, index) => {
      if (user.id === state.currentUser.id) {
        state.userList[index].is_active = !state.userList[index].is_active
      }
    })
  },
  SET_LOAD_STATUS: (state, newLoadStatus) => {
    state.isLoading = newLoadStatus
  }
}

const actions = {
  getUsers: async ({ commit }) => {
    commit('SET_LOAD_STATUS', true)
    const response = await http.get('users')
    if (!response.error) {
      commit('SET_USER_LIST', response.data)
    }
    commit('SET_LOAD_STATUS', false)
  },
  getUser: ({ commit }, userId) => {
    commit('GET_USER', userId)
  },
  deleteUser: async ({ state, commit }) => {
    const response = await http.delete(`users/${state.currentUser.id}`)
    if (!response.error) {
      commit('SWITCH_USER_STATUS')
      template.hideModal('#user-status')
    }
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
