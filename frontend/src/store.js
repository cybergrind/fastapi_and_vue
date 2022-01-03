import { createStore } from 'vuex'

const store = createStore({
  state() {
    return {
      default: 1,
      authors: [],
    }
  },
  mutations: {
    increment(state) {
      state.default += 1
    },
    decrement(state) {
      state.default -= 1
    },
    setAuthors(state, authors) {
      state.authors = authors
    },
    SOCKET_ONOPEN() {},
  },
  actions: {
    echo(ctx, { msg }) {
      console.log(`Got ECHO msg: ${msg}`)
    },
  }
})

export default store
