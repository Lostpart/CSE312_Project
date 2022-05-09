import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from '@/plugins/vuetify'
import axios from 'axios'
import { io } from 'socket.io-client'
import store from './store'
import './mock'

import apiConfigDev from '../apiConfig/apiConfigDev.json'
import apiConfigProd from '../apiConfig/apiConfigProd.json'

if (process.env.NODE_ENV !== 'development') {
	axios.defaults.baseURL = apiConfigProd.api
	Vue.prototype.apiConfig = apiConfigProd
} else {
	axios.defaults.baseURL = apiConfigDev.api
	Vue.prototype.apiConfig = apiConfigDev
}

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

router.beforeEach((to, from, next) => {
	const userID = store.state.user.userID
	if (typeof userID === 'undefined' || userID === null || userID.length === 0) {
		if (to.name !== 'register' && to.name !== 'login' && to.name !== 'home' && to.name !== 'tictactoe') {
			alert('You need to sign in first')
			next({ name: 'login' })
		} else {
			next()
		}
	} else {
		if (to.name === 'register' || to.name === 'login') {
			alert('You already signed in')
			next({ name: 'messages' })
		} else {
			next()
		}
	}
})
