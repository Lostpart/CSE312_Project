import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from '@/plugins/vuetify' 
import { io } from "socket.io-client";

Vue.config.productionTip = false
new Vue({
  router,
  vuetify,
  io,
  render: h => h(App)
}).$mount('#app')
