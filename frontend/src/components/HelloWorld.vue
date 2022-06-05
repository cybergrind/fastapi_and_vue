<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <counter />
    <p>
      For a guide and recipes on how to configure / customize this project,<br />
      check out the
      <a href="https://cli.vuejs.org" target="_blank" rel="noopener"
        >vue-cli documentation</a
      >.
    </p>
    <h3>Authors</h3>
    <button @click="store.generate">Generate Random</button>
    <div v-for="author in authors" :key="author.id">
      {{ author.id }}: {{ author.first_name }} {{ author.last_name }}
    </div>

    <counter />

    <h3>Essential Links</h3>
    <ul>
      <li>
        <a href="https://vuejs.org" target="_blank" rel="noopener">Core Docs</a>
      </li>
      <li>
        <a href="https://forum.vuejs.org" target="_blank" rel="noopener"
          >Forum</a
        >
      </li>
      <li>
        <a href="https://news.vuejs.org" target="_blank" rel="noopener">News</a>
      </li>
    </ul>
    <h3>Ecosystem</h3>
    <ul>
      <li>
        <a href="https://router.vuejs.org" target="_blank" rel="noopener"
          >vue-router</a
        >
      </li>
      <li>
        <a href="https://vuex.vuejs.org" target="_blank" rel="noopener">vuex</a>
      </li>
      <li>
        <a
          href="https://github.com/vuejs/vue-devtools#vue-devtools"
          target="_blank"
          rel="noopener"
          >vue-devtools</a
        >
      </li>
      <li>
        <a href="https://vue-loader.vuejs.org" target="_blank" rel="noopener"
          >vue-loader</a
        >
      </li>
      <li>
        <a
          href="https://github.com/vuejs/awesome-vue"
          target="_blank"
          rel="noopener"
          >awesome-vue</a
        >
      </li>
    </ul>
  </div>
</template>

<script>
import counter from './counter.vue'
import { useStore } from '../store'
import { storeToRefs } from 'pinia'
import { defineComponent, onMounted, onUpdated } from 'vue'


export default defineComponent({
    name: 'HelloWorld',
    props: {
        msg: String,
    },
    setup() {
        const store = useStore()
        const { authors } = storeToRefs(store)

        onUpdated(() => {
            console.log('updated: ', authors)
        })

        onMounted(async ()=>{
            console.log('mounted')
            await store.initFromServer()
            console.log('Authors: ', authors)
        })

        return {
            authors,
            store,
        }
    },
    components: {
        counter
    },
})
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
