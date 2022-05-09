<template>
	<div>
		<v-spacer></v-spacer>
		<v-row>
			<v-col cols="4">
				<v-btn class="white--text" :color="color" @click="refreshUsersList" style="float: right" id="refresh_btn"> Refresh List</v-btn>
				<v-switch v-model="onlyActiveSwitch" label="Only active users"></v-switch>
				<v-list subheader max-height="10" v-if="updated">
					<v-list-item v-for="user in usersListWithAvatarName" :key="user.user_id" link v-show="user.active || !onlyActiveSwitch">
						<v-list-item-avatar :color="user.active ? color : 'grey'">
							<span class="white--text text-h5">{{ user.avatarName }}</span>
						</v-list-item-avatar>

						<v-list-item-content @click="changeCurrentFriend(user)">
							<v-list-item-title v-text="user.displayName"></v-list-item-title>
						</v-list-item-content>

						<v-list-item-icon>
							<v-icon :color="user.active ? color : 'grey'"> mdi-message-outline </v-icon>
						</v-list-item-icon>
					</v-list-item>
				</v-list>
			</v-col>
			<v-col v-show="isClicked">
				<v-toolbar :color="`${this.isCurrentFriendActive ? this.color : 'grey'}`" dark>
					<v-toolbar-title>{{ currentFriendDisplayName }}</v-toolbar-title>
				</v-toolbar>
				<div id="chatView" style="height: 380px" class="overflow-y-auto overflow-x-hidden">
					<v-sheet color="white" min-height="300" width="100%">
						<div v-for="(chat, idx) in currentHistory" :key="idx">
							<v-row>
								<v-col>
									<v-card
										disabled
										elevation="4"
										link
										min-width="50px"
										class="pa-2 ma-4"
										style="display: inline-block"
										:color="chat.flag ? '#ffffff' : color"
										:class="{ 'white--text': !chat.flag }"
										:style="{ float: chat.flag ? 'left' : 'right' }"
									>
										{{ chat.message }}
									</v-card>
								</v-col>
							</v-row>
						</div>
					</v-sheet>
				</div>
				<v-sheet color="white" width="100%">
					<v-textarea
						id="msgInput"
						name="input-7-1"
						filled
						label="Message"
						placeholder="Enter message here"
						v-model="currentSentence"
					>
					</v-textarea>
					<v-btn style="float: right" @click="sendMsg">
						SEND
						<v-icon right> mdi-send </v-icon>
					</v-btn>
				</v-sheet>
			</v-col>
		</v-row>
	</div>
</template>

<script>
	import axios from 'axios'
	export default {
		components: {},
		mounted() {
			setInterval(()=>{
				const refresh_btn = document.getElementById('refresh_btn')
				refresh_btn.click()
			}, 1000)
			// const _this = this
			// setInterval(() => {
			// 	this.currentHistory = this.$store.state.user.chatHistory[this.currentFriendUserID]
			// }, 1000)
			// setInterval(() => {
			// 	axios
			// 		.get(axios.defaults.baseURL + 'allusers')
			// 		.then(function (response) {
			// 			const usersList = response.data
			// 			const userID = _this.$store.state.user.userID
			// 			_this.$store.commit('setUsersList', usersList)
			// 			if (usersList && userID && userID.length > 0) {
			// 				for (let i = 0; i < usersList.length; i++) {
			// 					axios
			// 						.post(axios.defaults.baseURL + 'chatHistory', { from: userID, to: usersList[i]['user_id'] })
			// 						.then(function (response) {
			// 							const historyArr = response['data']
			// 							if (!historyArr) return
			// 							for (let i = 0; i < historyArr.length; i++) {
			// 								historyArr[i]['flag'] = historyArr[i]['from'] !== userID
			// 							}
			// 							_this.$store.commit('setChatHistory', { user_id: usersList[i]['user_id'], history: historyArr })
			// 						})
			// 						.catch(function (error) {
			// 							console.log(error)
			// 						})
			// 				}
			// 			}
			// 		})
			// 		.catch(function (error) {
			// 			console.log(error)
			// 		})
			// }, 2000)
		},
		data: () => ({
			updated: true,
			onlyActiveSwitch: false,
			isCurrentFriendActive: false,
			currentFriend: '',
			currentFriendDisplayName: '',
			currentSentence: '',
			currentFriendUserID: null,
			isClicked: false,
			currentHistory: [],
		}),
		computed: {
			// currentHistory() {
			// 	return this.$store.state.user.chatHistory[this.currentFriendUserID]
			// },
			color() {
				return this.$store.state.user.color
			},
			usersListWithAvatarName() {
				const usersList = this.$store.state.user.usersList.filter((user) => user.user_id !== this.$store.state.user.userID)
				if (!usersList) return []
				else {
					for (let i = 0; i < usersList.length; i++) {
						usersList[i]['avatarName'] = usersList[i]['displayName'].substring(0, 1).toUpperCase()
					}
				}
				return usersList
			},
		},
		watch: {
			currentHistory() {
				this.updated = false
				this.$nextTick(() => {
					this.updated = true
				})
			},
		},
		methods: {
			refreshUsersList() {
				const _this = this
				axios
					.get(axios.defaults.baseURL + 'allusers')
					.then(function (response) {
						_this.$store.commit('setUsersList', response.data)
						const usersList = response.data
						const userID = _this.$store.state.user.userID
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
					})
					.catch(function (error) {
						console.log(error)
					})
			},
			changeCurrentFriend(user) {
				this.currentFriendUserID = user.user_id
				this.currentFriendDisplayName = user.displayName
				this.isCurrentFriendActive = user.active
				this.isClicked = true
				this.currentSentence = ''

				// const res = this.$store.state.user.chatHistory[this.currentFriendUserID]
				// if (!res || res.length == 0) this.currentHistory = []
				// else this.currentHistory = res
				setTimeout(() => {
					const chatView = document.getElementById('chatView')
					chatView.scrollTop = chatView.scrollHeight
				}, 1)
			},
			sendMsg() {
				const chatObj = {
					from: this.$store.state.user.userID,
					to: this.currentFriendUserID,
					message: this.currentSentence,
				}
				this.$store.commit('addChatHistory', {
					incoming: false,
					data: chatObj,
				})
				this.$store.state.user.webSocket.emit('send_chat', chatObj)
				this.currentSentence = ''
				setTimeout(() => {
					const chatView = document.getElementById('chatView')
					chatView.scrollTop = chatView.scrollHeight
				}, 50)
			},
		},
	}
</script>
