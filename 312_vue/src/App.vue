<template>
	<v-app>
		<!-- <v-navigation-drawer app width="400"> -->
		<v-navigation-drawer width="220" v-model="drawer" class="pa-0" app>
			<v-sheet color="blue lighten-4" class="pa-0">
				<v-list>
					<v-list-item>
						<v-list-item-avatar color="blue" size="60">
							<span class="white--text text-h5">{{currentUserAvatarName}}</span>
						</v-list-item-avatar>
					</v-list-item>
					<v-list-item link>
						<v-list-item-content>
							<v-list-item-title class="text-h6"> {{this.$store.state.user.displayName}} </v-list-item-title>
						</v-list-item-content>

						<v-list-item-action>
							<v-icon>mdi-menu-down</v-icon>
						</v-list-item-action>
					</v-list-item>
				</v-list>
			</v-sheet>

			<v-divider></v-divider>

			<v-list>
				<v-list-item v-for="[icon, text, route] in links" :key="icon" link>
					<v-list-item-icon>
						<v-icon>{{ icon }}</v-icon>
					</v-list-item-icon>
					<v-list-item-content @click="$router.replace(route).catch((err) => {})">
						<v-list-item-title>{{ text }}</v-list-item-title>
					</v-list-item-content>
				</v-list-item>
			</v-list>
		</v-navigation-drawer>
		<v-main>
			<v-container fluid>
				<router-view></router-view>
			</v-container>
		</v-main>

		<v-footer app color="transparent" height="40" inset>
			<div class="text-center">
				<v-btn dark @click="snackbar = true"> Check Socket Status </v-btn>
				<v-snackbar v-model="snackbar">
					{{ text }}

					<template v-slot:action="{ attrs }">
						<v-btn color="pink" text v-bind="attrs" @click="snackbar = false"> Close </v-btn>
					</template>
				</v-snackbar>
			</div>
		</v-footer>
	</v-app>
</template>

<script>
	// import DashBoard from './pages/DashBoard'
	import { io } from 'socket.io-client'

	export default {
		name: 'App',
		components: {
			// HelloWorld,
			// CardsStack,
			// DashBoard
		},
		computed:{
			currentUserAvatarName(){
				const displayName = this.$store.state.user.displayName
				if(displayName && displayName.length > 0) return displayName.substring(0, 1).toUpperCase() 
				return ''
			}
		},
		data: () => ({
			snackbar: false,
			text: '',
			drawer: null,
			links: [
				['mdi-message-text', 'Messages', '/messages'],
				['mdi-account-multiple', 'Square', '/square'],
				['mdi-account-plus', 'Register', '/register'],
				['mdi-account', 'Log In', '/login'],
				['mdi-electron-framework', 'Moments', '/moments'],
			],
		}),
		methods: {
			reserve() {
				this.loading = true
				setTimeout(() => (this.loading = false), 2000)
			},
		},
		mounted() {
			const socket = io('http://127.0.0.1:8080', {
				transports: ['websocket', 'polling'],
			})

			socket.on('connect_error', (err) => {
				this.text = err
				this.snackbar = true
			})
			socket.on('connect', (resp) => {
				this.text = socket.id + ' ' + resp.data
				this.snackbar = true
				this.$store.commit('setWebSocket', socket)
			})
			socket.on('disconnect', () => {
				this.text = 'Disconnected'
				this.snackbar = true
			})
			socket.on('new_chat', () => {
				this.text = 'Disconnected'
				this.snackbar = true
			})
		},
	}
</script>

<style>
	#app {
		font-family: Avenir, Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
		color: #2c3e50;
	}

	nav {
		padding: 30px;
	}

	nav a {
		font-weight: bold;
		color: #2c3e50;
	}

	nav a.router-link-exact-active {
		color: #42b983;
	}
</style>
