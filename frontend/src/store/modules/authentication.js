import http from '@/utilities/http'
import host from '@/utilities/host'
import admin from '@/router/admin'
import tenant from '@/router/tenant'

const USER = 'user'
const TOKEN = 'token'

const state = {
  user: localStorage.getItem(USER) ? JSON.parse(localStorage.getItem(USER)) : {},
  token: localStorage.getItem(TOKEN)
}

const getters = {
  logged: state => !!state.token
}

const mutations = {
  SET_USER: (state, newUser) => {
    let user = newUser || {}
    state.user = user
    localStorage.setItem(USER, JSON.stringify(user))
  },
  SET_TOKEN: (state, newToken) => {
    let token = newToken || null
    state.token = token
    localStorage.setItem(TOKEN, token)
  }
}

const actions = {
  login: async ({ commit }, user) => {
    const response = await http.post('accounts/login/', user)
    if (!response.error) {
      commit('SET_USER', response.data.user)
      commit('SET_TOKEN', response.data.token)
      if (host.isAdmin()) {
        admin.push({ name: 'home' })
      } else {
        tenant.push({ name: 'home' })
      }
    } else {
      return response.data
    }

    return {}
  },
  logout: ({ commit }) => {
    commit('SET_USER')
    commit('SET_TOKEN')
    localStorage.removeItem(USER)
    localStorage.removeItem(TOKEN)
    if (host.isAdmin()) {
      admin.push({ name: 'login' })
    } else {
      tenant.push({ name: 'login' })
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
