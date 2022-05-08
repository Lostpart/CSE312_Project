<template>
	<v-app>
		<!-- <v-navigation-drawer app width="400"> -->
		<div id="name"></div>
		<v-overlay :value="overlay">
			<v-color-picker v-model="color" dot-size="25" hide-inputs swatches-max-height="200"></v-color-picker>
			<v-btn class="white--text" :color="color" @click="handleColorChange"> Confirm </v-btn>
		</v-overlay>
		<DMNotification
			style="position: absolute; top: 30px; right: 20px; z-index: 10"
			:DmSender="DmSender"
			:DmUserID="DmUserID"
			:DmMsg="DmMsg"
			v-show="DmDisplaying"
			:closeDM="closeDM"
		></DMNotification>
		<v-navigation-drawer width="220" v-model="drawer" class="pa-0" app>
			<v-sheet :color="this.$store.state.user.color" class="pa-0">
				<v-list>
					<v-list-item>
						<v-list-item-avatar color="#1c5cbc" size="60">
							<span class="white--text text-h5">{{ currentUserAvatarName }}</span>
						</v-list-item-avatar>
					</v-list-item>
					<v-list-item link>
						<v-list-item-content>
							<v-list-item-title class="text-h6">
								{{ this.$store.state.user.displayName }}
							</v-list-item-title>
						</v-list-item-content>

						<v-list-item-action>
							<v-icon>mdi-menu-down</v-icon>
						</v-list-item-action>
					</v-list-item>
				</v-list>
			</v-sheet>

			<v-divider></v-divider>

			<v-list>
				<v-list-item v-for="[icon, text, route, showWhenLoggedIn] in links" :key="icon" link v-show="loggedIn === showWhenLoggedIn">
					<v-list-item-icon >
						<v-icon>{{ icon }}</v-icon>
					</v-list-item-icon>
					<v-list-item-content @click="$router.replace(route).catch((err) => {})">
						<v-list-item-title>{{ text }}</v-list-item-title>
					</v-list-item-content>
				</v-list-item>
				<v-list-item v-show="loggedIn === true">
					<v-list-item-icon>
						<v-list-item-content @click="logout">
							<v-list-item-title> Log out </v-list-item-title>
						</v-list-item-content>
					</v-list-item-icon>
				</v-list-item>
				<v-avatar :color="this.$store.state.user.color" @click="overlay = true" size="36"> </v-avatar>
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
	import { io } from 'socket.io-client'
	import axios from 'axios'
	import DMNotification from '@/components/DMNotification.vue'

	export default {
		name: 'App',
		components: {
			DMNotification,
		},
		created() {
			window.addEventListener('beforeunload', (e) => this.beforeunloadFn(e))
		},
		beforeDestroy() {
			// this.socket.emit('join', {
			//   displayName: 'Cusanity',
			//   room: 'cse312',
			// })
		},
		computed: {
			currentUserAvatarName() {
				const displayName = this.$store.state.user.displayName
				if (displayName && displayName.length > 0) return displayName.substring(0, 1).toUpperCase()
				return ''
			},
			avatarColor() {
				return this.color + ' darken-3'
			},
			loggedIn(){
				return this.$store.state.user.loggedIn === true
			}
		},
		watch: {
			// whenever question changes, this function will run
			color(newColor) {
				this.$store.commit('setColor', newColor)
			},
		},
		data: () => ({
			overlay: false,
			DmSender: '',
			DmMsg: '',
			DmDisplaying: false,
			DmUserID: '',
			snackbar: false,
			text: '',
			color: '#1c5cbc',
			// avatarColor: '',
			drawer: null,
			socket: null,
			links: [
				['mdi-account-plus', 'Register', '/register', false],
				['mdi-account', 'Log In', '/login', false],
				['mdi-message-text', 'Messages', '/messages', true],
				['mdi-electron-framework', 'Moments', '/moments', true],
				['mdi-gamepad-circle-outline', 'Game', '/tictactoe', false],
				// ['mdi-account-multiple', 'Square', '/square'],
			],
		}),
		methods: {
			closeDM() {
				this.DmDisplaying = false
			},
			logout() {
				const ws = this.$store.state.user.webSocket
				const displayName = this.$store.state.user.displayName
				const userID = this.$store.state.user.userID
				if (ws) {
					ws.emit('leave', {
						displayName: displayName,
						room: userID,
					})
				}
				this.$store.commit('clearChatHistory')
				this.$store.commit('clearDisplayName')
				this.$store.commit('clearEmail')
				this.$store.commit('clearColor')
				this.$store.commit('clearUserID')
				this.$store.commit('setLoggedIn', false)
			},
			handleColorChange() {
				this.overlay = false
				axios
					.post('http://127.0.0.1:8080/settings', { user_id: this.$store.state.user.userID, color: this.$store.state.user.color })
					.then(function (response) {
						if (response.data && response.data.status) {
							if (response.data.status === true) alert('Color setting updated')
							else if (response.data.message) {
								console.log(response.data.message)
							}
						}
					})
					.catch(function (error) {
						console.log(error)
					})
			},
			beforeunloadFn(e) {
				const displayName = this.$store.state.user.displayName
				const userID = this.$store.state.user.userID
				if (!displayName || displayName.length === 0 || !userID || userID.length === 0) return
				this.socket.emit('leave', {
					displayName: displayName,
					room: userID,
				})
				e.preventDefault()
			},
			reserve() {
				this.loading = true
				setTimeout(() => (this.loading = false), 2000)
			},
			getUsernameById(userID) {
				const usersList = this.$store.state.user.usersList
				console.log(usersList)
				for (let i = 0; i < usersList.length; i++) {
					if (usersList[i]['user_id'] === userID) return usersList[i]['displayName']
				}
				return ''
			},
		},
		mounted() {
			const beforeUnloadListener = (event) => {
				event.preventDefault()
				return (event.returnValue = 'Are you sure you want to exit?')
			}

			const nameInput = document.querySelector('#name')

			nameInput.addEventListener('input', (event) => {
				if (event.target.value !== '') {
					addEventListener('beforeunload', beforeUnloadListener, { capture: true })
				} else {
					removeEventListener('beforeunload', beforeUnloadListener, { capture: true })
				}
			})
			window.onbeforeunload = () => {
				this.clearViews()
				return 'tips'
			}
			const _this = this
			const socket = io('http://127.0.0.1:8080', {
				transports: ['websocket', 'polling'],
			})

			socket.on('connect_error', (err) => {
				this.text = err
				this.snackbar = true
			})
			socket.on('connect', (resp) => {
				this.text = resp && resp.data ? socket.id + ' ' + resp.data : ''
				this.snackbar = true
				this.$store.commit('setWebSocket', socket)
				this.socket = socket
			})
			socket.on('disconnect', () => {
				this.text = 'Disconnected'
				this.snackbar = true
			})
			socket.on('new_chat', (resp) => {
				const newChatObj = JSON.parse(resp)
				if (newChatObj['from'] === this.$store.state.user.userID) return
				const sender = this.getUsernameById(newChatObj['from'])

				const _this = this
				if (!sender) {
					const userID = this.$store.state.user.userID
					axios
						.get('http://127.0.0.1:8080/allusers')
						.then(function (response) {
							_this.$store.commit('setUsersList', response.data)
							console.log(response.data)
							axios
								.post('http://127.0.0.1:8080/chatHistory', { from: newChatObj['from'], to: userID })
								.then(function (response) {
									const historyArr = response['data']
									if (!historyArr) return
									for (let i = 0; i < historyArr.length; i++) {
										historyArr[i]['flag'] = historyArr[i]['from'] !== userID
									}
									_this.$store.commit('setChatHistory', { user_id: newChatObj['from'], history: historyArr })
									_this.DmUserID = newChatObj['from']
									_this.DmSender = _this.getUsernameById(newChatObj['from'])
									_this.DmMsg = newChatObj['message']
									_this.DmDisplaying = true
								})
								.catch(function (error) {
									console.log(error)
								})
						})
						.catch(function (error) {
							console.log(error)
						})
				} else {
					this.$store.commit('addChatHistory', { incoming: true, data: newChatObj })
					this.DmUserID = newChatObj['from']
					this.DmSender = this.getUsernameById(newChatObj['from'])
					this.DmMsg = newChatObj['message']
					this.DmDisplaying = true
				}
				setTimeout(() => {
					const chatView = document.getElementById('chatView')
					if (chatView) chatView.scrollTop = chatView.scrollHeight
				}, 50)
			})
			socket.on('update_map', (resp) => {
				const mapObj = JSON.parse(resp)
				this.$store.commit('setMap', mapObj['map'])
				this.$store.commit('setResult', mapObj['result'])
				this.$store.commit('setFinished', mapObj['finished'])
				this.$store.commit('setN', mapObj['n'])
			})
			socket.on('moment_like', (resp) => {
				const momentUpdateObj = JSON.parse(JSON.parse(resp))
				_this.$store.commit('updateMomentsList', momentUpdateObj)
			})
			axios
				.get('http://127.0.0.1:8080/allusers')
				.then(function (response) {
					_this.$store.commit('setUsersList', response.data)
				})
				.catch(function (error) {
					console.log(error)
				})
			axios
				.post('http://127.0.0.1:8080/moment/getRecentMoments', { limit: 100 })
				.then(function (response) {
					_this.$store.commit('setMomentsList', response.data)
				})
				.catch(function (error) {
					console.log(error)
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
