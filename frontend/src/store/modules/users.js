import http from '@/utilities/http'
import template from '@/utilities/template'

const state = {
  users: [],
  user: {},
  errors: {},
  isLoading: false
}

const getters = {
  isNewUser: state => state.user.id === undefined
}

const mutations = {
  SET_USERS: (state, newUsers) => {
    state.users = newUsers
  },
  SET_USER: (state, newUser) => {
    state.users = [
      ...state.users.filter(user => user.id !== newUser.id),
      newUser
    ]
  },
  SET_ERRORS: (state, newErrors) => {
    state.errors = newErrors || {}
  },
  ADD_USER: (state, newUser) => {
    state.users.unshift(newUser)
  },
  GET_USER: (state, userId) => {
    state.user = state.users.find(user => user.id === userId) || {}
  },
  SWITCH_USER_STATUS: state => {
    state.users.forEach((user, index) => {
      if (user.id === state.user.id) {
        state.users[index].is_active = !state.users[index].is_active
      }
    })
  },
  SET_LOAD_STATUS: (state, newLoadStatus) => {
    state.isLoading = newLoadStatus
  },
  SET_USERNAME: (state, newUsername) => {
    state.user = { ...state.user, username: newUsername }
  },
  SET_EMAIL: (state, newEmail) => {
    state.user = { ...state.user, email: newEmail }
  },
  SET_FIRST_NAME: (state, newFirstName) => {
    state.user = { ...state.user, first_name: newFirstName }
  },
  SET_LAST_NAME: (state, newLastName) => {
    state.user = { ...state.user, last_name: newLastName }
  },
  SET_PASSWORD: (state, newPassword) => {
    state.user = { ...state.user, password: newPassword }
  },
  SET_PASSWORD_CONFIRMATION: (state, newPasswordConfirmation) => {
    state.user = { ...state.user, password_confirmation: newPasswordConfirmation }
  }
}

const actions = {
  getUsers: async ({ commit }) => {
    commit('SET_LOAD_STATUS', true)
    const response = await http.get('accounts/users/')
    if (!response.error) {
      commit('SET_USERS', response.data)
    }
    commit('SET_LOAD_STATUS', false)
  },
  getUser: ({ commit }, userId) => {
    commit('SET_ERRORS')
    commit('GET_USER', userId)
  },
  createUser: async ({ state, commit }, event) => {
    if (event) event.preventDefault()
    commit('SET_ERRORS')
    const response = await http.post('accounts/users/', state.user)
    if (!response.error) {
      commit('ADD_USER', response.data)
      template.hideModal('#user-form')
      commit('GET_USER')
    } else {
      commit('SET_ERRORS', response.data)
    }
  },
  updateUser: async ({ state, commit }, event) => {
    if (event) event.preventDefault()
    commit('SET_ERRORS')
    const response = await http.patch(`accounts/users/${state.user.id}/`, state.user)
    if (!response.error) {
      commit('SET_USER', response.data)
      template.hideModal('#user-form')
    } else {
      commit('SET_ERRORS', response.data)
    }
  },
  deleteUser: async ({ state, commit }) => {
    const response = await http.delete(`accounts/users/${state.user.id}/`)
    if (!response.error) {
      commit('SWITCH_USER_STATUS')
      template.hideModal('#user-status')
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
