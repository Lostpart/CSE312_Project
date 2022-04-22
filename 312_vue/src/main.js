import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from '@/plugins/vuetify' 
import axios from "axios";
import { io } from "socket.io-client";

Vue.config.productionTip = false
new Vue({
  router,
  vuetify,
  axios,
  io,
  render: h => h(App)
}).$mount('#app')
