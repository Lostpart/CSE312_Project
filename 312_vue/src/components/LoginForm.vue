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
							this.$store.commit('setDisplayName', response.data['displayName'])
							this.$store.commit('setEmail', response.data['email'])
							this.$store.commit('setUserID', response.data['user_id'])
						}
					})
					.catch((error) => alert(error))
				const usersList = this.$store.state.user.usersList
				const userID = this.$store.state.user.userID
				if (usersList && userID) {
					for (let i = 0; i < usersList.length; i++) {
						axios
							.post('http://127.0.0.1:8080/chatHistory', { from: userID, to: usersList[i]['user_id'] })
							.then(function (response) {
								_this.$store.commit('setChatHistory', { user_id: usersList[i]['user_id'], history: response['data'] })
							})
							.catch(function (error) {
								console.log(error)
							})
					}
          console.log(this.$store.state.user.chatHistory)
				}
			},
			reset() {
				this.$refs.form.reset()
			},
		},
	}
</script>
