import http from '@/utilities/http'
import template from '@/utilities/template'

const state = {
  userList: [],
  currentUser: {},
  errorList: {},
  isLoading: false
}

const getters = {
  newUser: state => state.currentUser.id === undefined
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
  ADD_USER: (state, newUser) => {
    state.userList.push(newUser)
  },
  SET_LOAD_STATUS: (state, newLoadStatus) => {
    state.isLoading = newLoadStatus
  },
  SET_USERNAME: (state, newUsername) => {
    state.currentUser.username = newUsername
  },
  SET_FIRST_NAME: (state, newFirstName) => {
    state.currentUser.first_name = newFirstName
  },
  SET_LAST_NAME: (state, newLastName) => {
    state.currentUser.last_name = newLastName
  },
  SET_EMAIL: (state, newEmail) => {
    state.currentUser.email = newEmail
  },
  SET_PASSWORD: (state, newPassword) => {
    state.currentUser.password = newPassword
  },
  SET_PASSWORD_CONFIRMATION: (state, newPasswordConfirmation) => {
    state.currentUser.password_confirmation = newPasswordConfirmation
  },
  SET_ERRORS_LIST: (state, newErroList) => {
    state.errorList = newErroList
  }
}

const actions = {
  getUsers: async ({ commit }) => {
    commit('SET_LOAD_STATUS', true)
    const response = await http.get('users/')
    if (!response.error) {
      commit('SET_USER_LIST', response.data)
    }
    commit('SET_LOAD_STATUS', false)
  },
  getUser: ({ commit }, userId) => {
    commit('GET_USER', userId)
  },
  deleteUser: async ({ state, commit }) => {
    const response = await http.delete(`users/${state.currentUser.id}/`)
    if (!response.error) {
      commit('SWITCH_USER_STATUS')
      template.hideModal('#user-status')
    }
  },
  createUser: async ({ state, commit }, event) => {
    if (event) event.preventDefault()
    const response = await http.post('users/', state.currentUser)
    if (!response.error) {
      commit('ADD_USER', response.data)
      template.hideModal('#user-form')
      commit('GET_USER', 0)
      commit('SET_ERRORS_LIST', {})
    } else {
      commit('SET_ERRORS_LIST', response.data)
    }
  },
  updateUser: async ({ commit }, event) => {
    if (event) event.preventDefault()
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
