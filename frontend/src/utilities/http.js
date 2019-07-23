import axios from 'axios'

const http = axios.create({
  baseURL: 'http://localhost:8000/'
})

const CONNECTION_ERROR = {
  error: true,
  status: 400,
  statusText: 'Connection error 😿'
}

export default {
  get: async function (url) {
    try {
      return await http.get(url)
    } catch (error) {
      if (error.response) {
        error.response.error = true
        return error.response
      }
      return CONNECTION_ERROR
    }
  },
  post: async function (url, data) {
    try {
      return await http.post(url, data)
    } catch (error) {
      if (error.response) {
        error.response.error = true
        return error.response
      }
      return CONNECTION_ERROR
    }
  },
  delete: async function (url) {
    try {
      return await http.delete(url)
    } catch (error) {
      if (error.response) {
        error.response.error = true
        return error.response
      }
      return CONNECTION_ERROR
    }
  },
  patch: async function (url, data) {
    try {
      return await http.patch(url, data)
    } catch (error) {
      if (error.response) {
        error.response.error = true
        return error.response
      }
      return CONNECTION_ERROR
    }
  }
}
