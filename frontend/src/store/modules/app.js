import host from '@/utilities/host'

const state = {
  isAdmin: host.isAdmin()
}

export default {
  namespaced: true,
  state
}
