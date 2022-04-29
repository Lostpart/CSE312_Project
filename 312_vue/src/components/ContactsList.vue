<template>
	<div>
		<v-spacer></v-spacer>
		<v-row>
			<v-col cols="4">
				<v-list subheader max-height="10">
					<v-list-item v-for="user in usersListWithAvatarName" :key="user.user_id" link>
						<v-list-item-avatar color="blue">
							<span class="white--text text-h5">{{ user.avatarName }}</span>
						</v-list-item-avatar>

						<v-list-item-content @click="changeCurrentFriend(user)">
							<v-list-item-title v-text="user.displayName"></v-list-item-title>
						</v-list-item-content>

						<v-list-item-icon>
							<v-icon :color="user.active ? 'deep-purple accent-4' : 'grey'"> mdi-message-outline </v-icon>
						</v-list-item-icon>
					</v-list-item>
				</v-list>
			</v-col>
			<v-col v-show="isClicked">
				<v-toolbar color="blue" dark>
					<v-toolbar-title>{{ currentFriendDisplayName }}</v-toolbar-title>
				</v-toolbar>
				<v-sheet color="white" elevation="1" min-height="300" width="100%">
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
									:class="{ 'light-blue': !chat.flag, 'white--text': !chat.flag }"
									:style="{ float: chat.flag ? 'left' : 'right' }"
								>
									{{ chat.message }}
								</v-card>
							</v-col>
						</v-row>
					</div>
				</v-sheet>
				<v-sheet color="white" width="100%">
					<v-textarea name="input-7-1" filled label="Message" placeholder="Enter message here" v-model="currentSentence">
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
	export default {
		components: {},
		data: () => ({
			currentFriend: '',
			currentFriendDisplayName: '',
			currentSentence: '',
			currentFriendUserID: null,
			currentHistory: [],
			isClicked: false,
		}),
		computed: {
			usersListWithAvatarName() {
				const usersList = this.$store.state.user.usersList.filter(user=>user.user_id !== this.$store.state.user.userID)
				if (!usersList) return []
				else {
					for (let i = 0; i < usersList.length; i++) {
						usersList[i]['avatarName'] = usersList[i]['displayName'].substring(0, 1).toUpperCase()
					}
				}
				return usersList
			},
		},
		methods: {
			changeCurrentFriend(user) {
				this.currentFriendUserID = user.user_id
				this.currentFriendDisplayName = user.displayName
				// this.currentHistory = chat.history
				this.isClicked = true
				this.currentSentence = ''
				const res = this.$store.state.user.chatHistory[this.currentFriendUserID]
				for (let i = 0; i < res.length; i++) {
					res[i]['flag'] = res[i]['from'] !== this.$store.state.user.userID
				}
				this.currentHistory = res
			},
			sendMsg() {
				const friend_idx = this.findFriendIdx(this.currentFriend)
				this.recent[friend_idx]['history'].push({
					chatID: Math.random() * 10000,
					timestamp: '2022-04-15 03:44:36',
					msg: this.currentSentence,
				})
				this.recent[friend_idx]['history'].push({
					flag: true,
					chatID: Math.random() * 10000,
					timestamp: '2022-04-15 03:44:36',
					msg: this.currentSentence,
				})
				this.currentSentence = ''
			},
		},
	}
</script>
