<template>
	<v-form ref="form" v-model="valid" lazy-validation>
		<v-text-field v-model="email" :rules="emailRules" label="E-mail" required></v-text-field>

		<v-text-field v-model="password" label="Password" required></v-text-field>

		<v-btn :disabled="!valid" color="success" class="mr-4" @click="login"> LOGIN </v-btn>

		<v-btn color="error" class="mr-4" @click="reset"> Reset Form </v-btn>
	</v-form>
</template>

<script>
	import axios from 'axios'

	export default {
		data: () => ({
			valid: true,
			email: '1@12.com',
			emailRules: [(v) => !!v || 'E-mail is required', (v) => /.+@.+\..+/.test(v) || 'E-mail must be valid'],
			password: '1',
		}),

		methods: {
			login() {
				const _this = this
				const loginJson = {}
				loginJson['email'] = this.email
				loginJson['password'] = this.password
				axios
					.post('http://127.0.0.1:8080/login', loginJson)
					.then((response) => {
						if (response.data.status === 'Error') {
							alert(response.data['message'])
						} else {
							_this.$store.commit('setDisplayName', response.data['displayName'])
							_this.$store.commit('setEmail', response.data['email'])
							_this.$store.commit('setUserID', response.data['user_id'])
							console.log(response.data)
							_this.$store.commit('setColor', response.data['settings'])
							this.$store.state.user.webSocket.emit('join', {
								displayName: response.data['displayName'],
								room: response.data['user_id'],
							})
							const usersList = this.$store.state.user.usersList
							const userID = response.data['user_id']
							if (usersList && userID) {
								for (let i = 0; i < usersList.length; i++) {
									axios
										.post('http://127.0.0.1:8080/chatHistory', { from: userID, to: usersList[i]['user_id'] })
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
