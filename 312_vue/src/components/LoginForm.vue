<template>
	<v-form ref="form" v-model="valid" lazy-validation>
		<v-text-field v-model="email" :rules="emailRules" label="E-mail" required></v-text-field>

		<v-text-field type="password" v-model="password" label="Password" required></v-text-field>

		<v-btn :disabled="!valid" color="success" class="mr-4" @click="login"> LOGIN </v-btn>

		<v-btn color="error" class="mr-4" @click="reset"> Reset Form </v-btn>
	</v-form>
</template>

<script>
	import axios from 'axios'

	export default {
		data: () => ({
			valid: true,
			email: '',
			emailRules: [(v) => !!v || 'E-mail is required', (v) => /.+@.+\..+/.test(v) || 'E-mail must be valid'],
			password: '',
		}),

		methods: {
			login() {
				const ws = this.$store.state.user.webSocket
				const displayName = this.$store.state.user.displayName
				const userID = this.$store.state.user.userID
				if (ws && displayName && userID) {
					ws.emit('leave', {
						displayName: displayName,
						room: userID,
					})
				}
				const _this = this
				const loginJson = {}
				loginJson['email'] = this.email
				loginJson['password'] = this.password
				axios
					.post(axios.defaults.baseURL + 'login', loginJson)
					.then((response) => {
						if (response.data.status === 'Error') {
							alert(response.data['message'])
						} else {
							_this.$store.commit('setDisplayName', response.data['displayName'])
							_this.$store.commit('setEmail', response.data['email'])
							_this.$store.commit('setUserID', response.data['user_id'])
							_this.$store.commit('setLoggedIn', true)
							console.log(response.data)
							_this.$store.commit('setColor', response.data['settings'])
							_this.$store.state.user.webSocket.emit('join', {
								displayName: response.data['displayName'],
								room: response.data['user_id'],
							})
							const usersList = _this.$store.state.user.usersList
							const userID = response.data['user_id']
							if (usersList && userID) {
								for (let i = 0; i < usersList.length; i++) {
									axios
										.post(axios.defaults.baseURL + 'chatHistory', { from: userID, to: usersList[i]['user_id'] })
										.then(function (response) {
											const historyArr = response['data']
											if (!historyArr) return
											for (let i = 0; i < historyArr.length; i++) {
												historyArr[i]['flag'] = historyArr[i]['from'] !== userID
											}
											_this.$store.commit('setChatHistory', { user_id: usersList[i]['user_id'], history: historyArr })
										})
										.catch(function (error) {
											console.log(error)
										})
								}
							}
							_this.$router.push({ name: 'messages' })
						}
					})
					.catch((error) => alert(error))
			},
			reset() {
				this.$refs.form.reset()
			},
		},
	}
</script>
