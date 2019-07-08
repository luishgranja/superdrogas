import axios from 'axios'

const http = axios.create({
  baseURL: 'http://localhost:8000/'
})

const CONNECTION_ERROR = {
  error: true,
  status: 400,
  statusText: 'Connection error'
}

export default {
  get: async function (url) {
    try {
      return await http.get(url)
    } catch (error) {
      return CONNECTION_ERROR
    }
  },
  delete: async function (url) {
    try {
      return await http.delete(url)
    } catch (error) {
      return CONNECTION_ERROR
    }
  }
}
