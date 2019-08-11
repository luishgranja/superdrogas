import http from '@/utilities/http'
// import router from '@/router'

const USER = 'user'
const TOKEN = 'token'

const state = {
  token: localStorage.getItem(TOKEN),
  user: {},
  errors: {}
}

const getters = {
  logged: state => !!state.token
}

const mutations = {
  SET_TOKEN: (state, newToken) => {
    var token = newToken || null
    state.token = token
    localStorage.setItem(TOKEN, token)
  },
  SET_USER: (state, newUser) => {
    state.user = newUser || {}
  },
  SET_USERNAME: (state, newUsername) => {
    state.user = { ...state.user, username: newUsername }
  },
  SET_PASSWORD: (state, newPassword) => {
    state.user = { ...state.user, password: newPassword }
  },
  SET_ERRORS: (state, newErrors) => {
    state.errors = newErrors || {}
  }
}

const actions = {
  async login ({ state, commit }) {
    commit('SET_ERRORS')
    const response = await http.post('rest-auth/login/', state.user)
    if (!response.error) {
      console.log(response.data.key)
      commit('SET_TOKEN', response.data.key)
      // router.push({ name: 'home' })
    } else {
      commit('SET_ERRORS', response.data)
    }
  },
  logout ({ commit }) {
    commit('SET_USER')
    commit('SET_TOKEN')
    localStorage.removeItem(USER)
    localStorage.removeItem(TOKEN)
    // router.push({ name: 'login' })
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
