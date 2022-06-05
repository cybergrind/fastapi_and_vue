import { createApp } from 'vue'
import App from './App.vue'
import { useStore } from './store'
import VueNativeSock from 'vue-native-websocket-vue3'
import { createPinia } from 'pinia'

const pinia = createPinia()
const app = createApp(App)

app.use(pinia)
app.use(VueNativeSock, `ws://${location.host}/api/ws`, {
  store: useStore(pinia),
  reconnection: true,
  format: 'json',
})
app.mount('#app')
