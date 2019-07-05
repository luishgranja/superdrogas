import axios from 'axios'

const http = axios.create({
  baseURL: 'http://localhost:8000/'
})

const get = async function (url) {
  try {
    const response = await http.get(url)
    return response.data
  } catch (error) {
    return {
      status: 400,
      statusText: 'Connection refused 😾'
    }
  }
}

export default {
  get
}
