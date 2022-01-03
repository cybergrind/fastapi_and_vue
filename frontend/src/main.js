import { createApp } from 'vue'
import App from './App.vue'
import store from './store'
import VueNativeSock from "vue-native-websocket-vue3"

const app = createApp(App)
app.use(VueNativeSock, `ws://${location.host}/api/ws`, {
  store: store,
  reconnection: true,
  format: 'json',
})
app.use(store)
app.mount('#app')
