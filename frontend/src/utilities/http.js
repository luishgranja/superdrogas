import axios from 'axios'
import host from './host'

var http = axios.create({
  baseURL: `http://${host.isAdmin() ? '' : host.getSubdomain() + '.'}localhost:8000/api/`
})

const CONNECTION_ERROR = {
  error: true,
  status: 400,
  statusText: 'Connection error. 😿'
}

const errorHandler = (error) => {
  if (error.response) {
    error.response.error = true
    return error.response
  }
  return CONNECTION_ERROR
}

export default {
  get: async (url) => {
    try {
      return await http.get(url)
    } catch (error) {
      return errorHandler(error)
    }
  },
  post: async (url, data) => {
    try {
      return await http.post(url, data)
    } catch (error) {
      return errorHandler(error)
    }
  },
  delete: async (url) => {
    try {
      return await http.delete(url)
    } catch (error) {
      return errorHandler(error)
    }
  },
  patch: async (url, data) => {
    try {
      return await http.patch(url, data)
    } catch (error) {
      return errorHandler(error)
    }
  }
}
