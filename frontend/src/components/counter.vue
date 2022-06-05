<template>
  <div class="counter">
    <div>Default: {{ store.default }}</div>
    <button v-on:click="increment">INC</button>
    <button @click="decrement">DEC</button>
  </div>
</template>

<script>
import { useStore } from '../store'
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'counter',
  setup() {
    const store = useStore()
    const { increment, decrement } = store
    return {
      store,
      increment,
      decrement,
    }
  },
})
</script>

<style scoped>
.counter {
  border: solid;
  display: inline-block;
  padding: 0.5em;
  margin-top: 1em;
}
</style>
