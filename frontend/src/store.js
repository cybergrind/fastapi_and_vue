import { createStore } from 'vuex'

const store = createStore({
  state() {
    return {
      default: 1,
    }
  },
  mutations: {
    increment(state) {
      state.default += 1
    },
    decrement(state) {
      state.default -= 1
    },
  },
})

export default store
