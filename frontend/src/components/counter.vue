<template>
  <div class="counter">
    <div>Default: {{ store.default }}</div>
    <button v-on:click="increment">INC</button>
    <button @click="decrement">DEC</button>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'counter',
  computed: mapState({ store: (state) => state }),
  methods: {
    increment() {
      this.$store.commit('increment')
    },
    decrement() {
      this.$store.commit('decrement')
    },
  },
}
</script>

<style scoped>
.counter {
  border: solid;
  display: inline-block;
  padding: 0.5em;
  margin-top: 1em;
}
</style>
