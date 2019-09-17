import http from '@/utilities/http'
import template from '@/utilities/template'

const state = {
  tenants: [],
  tenant: {},
  errors: {},  
  isLoading: false,
  inactiveTenants: [],
  churn: 0.0
}

const getters = {
  isNewTenant: state => state.tenant.id === undefined,
  inactiveTenants: state => {
    
    state.inactiveTenants = [0,0,0,0,0,0,0,0,0]
    for (var month = 1; month <= 9; month++) {   
      state.tenants.forEach(tenant => {
        var dateCheck = tenant.date_inactive
        if(dateCheck !== null ){
          var dateFrom = "0" + month + "/01/2019"
        var dateTo = "0" + month + "/27/2019"        
        
        var d1 = dateFrom.split("/")
        var d2 = dateTo.split("/")
        var c = dateCheck.split("-")
  
        var from = new Date(d1[2], parseInt(d1[0])-1, d1[1])
        var to   = new Date(d2[2], parseInt(d2[0])-1, d2[1])
        var check = new Date(c[0], parseInt(c[1])-1, c[2])

        if (check > from && check < to){
          state.inactiveTenants[month-1]++
        }
      }
    })
  }
  return state.inactiveTenants
  },
  activeTenants: state => {
    var tenants = []
    state.tenants.forEach(tenant => {
      if (tenant.is_active) {
        tenants.push(tenant)
      }
    })
    return tenants
  }  
}

const mutations = {
  SET_TENANTS: (state, newTenants) => {
    state.tenants = newTenants
  },
  SET_TENANT: (state, newTenant) => {
    state.tenants = [
      ...state.tenants.filter(tenant => tenant.id !== newTenant.id),
      newTenant
    ]
  },
  SET_ERRORS: (state, newErrors) => {
    state.errors = newErrors || {}
  },
  SET_INACTIVE_TENANTS: (state, getters) => {
    state.inactiveTenants = getters.inactiveTenants
    state.churn = state.inactiveTenants[8]/(getters.activeTenants.length-1)

  },
  ADD_TENANT: (state, newTenant) => {
    state.tenants.unshift(newTenant)
  },
  GET_TENANT: (state, tenantId) => {
    state.tenant = state.tenants.find(tenant => tenant.id === tenantId) || {}
  },
  SWITCH_TENANT_STATUS: state => {
    state.tenants.forEach((tenant, index) => {
      if (tenant.id === state.tenant.id) {
        state.tenants[index].is_active = !state.tenants[index].is_active
      }
    })
  },
  SET_LOAD_STATUS: (state, newLoadStatus) => {
    state.isLoading = newLoadStatus
  },
  SET_SCHEMA_NAME: (state, newSchemaName) => {
    state.tenant = { ...state.tenant, schema_name: newSchemaName }
  },
  SET_NAME: (state, newName) => {
    state.tenant = { ...state.tenant, name: newName }
  },
  SET_PREFIX: (state, newPrefix) => {
    state.tenant = { ...state.tenant, prefix: newPrefix }
  },
  SET_NIT: (state, newNit) => {
    state.tenant = { ...state.tenant, nit: newNit }
  },
  SET_PHONE: (state, newPhone) => {
    state.tenant = { ...state.tenant, phone: newPhone }
  },
  SET_EMAIL: (state, newEmail) => {
    state.tenant = { ...state.tenant, email: newEmail }
  },
  SET_ADDRESS: (state, newAddress) => {
    state.tenant = { ...state.tenant, address: newAddress }
  },
  SET_DESCRIPTION: (state, newDescription) => {
    state.tenant = { ...state.tenant, description: newDescription }
  }
}

const actions = {
  getTenants: async ({ commit }) => {
    commit('SET_LOAD_STATUS', true)
    const response = await http.get('pharmacies/')
    if (!response.error) {
      commit('SET_TENANTS', response.data)
    }
    commit('SET_LOAD_STATUS', false)
  },
  getTenant: ({ commit }, tenantId) => {
    commit('SET_ERRORS')
    commit('GET_TENANT', tenantId)
  },
  createTenant: async ({ state, commit }, event) => {
    if (event) event.preventDefault()
    commit('SET_ERRORS')
    const response = await http.post('pharmacies/', state.tenant)
    if (!response.error) {
      template.destroy()
      commit('ADD_TENANT', response.data)
      template.hideModal('#tenant-form')
      commit('GET_TENANT')
    } else {
      commit('SET_ERRORS', response.data)
    }
  },
  getInactiveTenants: async ({ commit, getters }) => {
    commit('SET_INACTIVE_TENANTS', getters)
  },
  updateTenant: async ({ state, commit }, event) => {
    if (event) event.preventDefault()
    commit('SET_ERRORS')
    const response = await http.patch(`pharmacies/${state.tenant.id}/`, state.tenant)
    if (!response.error) {
      template.destroy()
      commit('SET_TENANT', response.data)
      template.hideModal('#tenant-form')
    } else {
      commit('SET_ERRORS', response.data)
    }
  },
  deleteTenant: async ({ state, commit }) => {
    const response = await http.delete(`pharmacies/${state.tenant.id}/`)
    if (!response.error) {
      commit('SWITCH_TENANT_STATUS')
      template.hideModal('#tenant-status')
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
