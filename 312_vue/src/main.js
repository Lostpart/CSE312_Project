import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from '@/plugins/vuetify'
import axios from 'axios'
import { io } from 'socket.io-client'
import store from './store'
import './mock'

Vue.config.productionTip = false
new Vue({
	router,
	vuetify,
	axios,
	io,
	store,
	render: (h) => h(App),
}).$mount('#app')

Vue.prototype.webSocket = null
