import { defineStore } from 'pinia'
import axios from 'axios'
import { API_BASE } from './const'

const useStore = defineStore({
  id: 'fastapiStore',
  state: () => ({
    rawAuthors: [],
    default: 1,
  }),
  getters: {
    authors: (state) => {
      return state.rawAuthors.reduce((acc, i) => {
        acc.push(i)
        return acc
      }, [])
    },
  },
  actions: {
    increment() {
      this.default += 1
    },
    decrement() {
      this.default -= 1
    },
    async generate() {
      await axios.post(`${API_BASE}/author/generate`)
      let r = await axios.get(`${API_BASE}/author`)
      this.rawAuthors = r.data
    },
    async initFromServer() {
      axios.get(`${API_BASE}/author`).then((response) => {
        this.rawAuthors = response.data
      })
    },
    SOCKET_ONOPEN(){
      console.log('On socket open')
    },
    SOCKET_ONCLOSE(){
      console.log('On socket close')
    },
    SOCKET_ONMESSAGE(e){
      console.log('message: ', e)
    },
  },
})

export { useStore }

