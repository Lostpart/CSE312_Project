import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MessagesView from '../pages/MessagesView.vue'
import RegisterView from '../views/RegisterView.vue'
import LoginView from '../views/LoginView.vue'
import MomentsView from '../views/MomentsView.vue'
import TicTacToe from '../views/TicTacToe.vue'

Vue.use(VueRouter)

const routes = [
	{
		path: '/',
		name: 'home',
		component: HomeView,
	},
	{
		path: '/messages',
		name: 'messages',
		component: MessagesView,
	},
	{
		path: '/register',
		name: 'register',
		component: RegisterView,
	},
	{
		path: '/login',
		name: 'login',
		component: LoginView,
	},
	{
		path: '/moments',
		name: 'moments',
		component: MomentsView,
	},
	{
		path: '/tictactoe',
		name: 'tictactoe',
		component: TicTacToe,
	},
]

const router = new VueRouter({
	routes,
})

export default router
