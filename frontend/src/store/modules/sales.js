import http from '@/utilities/http'
import template from '@/utilities/template'

const state = {
  cart: [],
  products: [],
  errors: {},
  isLoading: false
}

export default {
  namespaced: true,
  state
}