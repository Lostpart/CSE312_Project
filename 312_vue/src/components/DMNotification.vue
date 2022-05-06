<template>
	<v-card class="mx-auto" min-width="344" outlined>
		<v-list-item three-line>
			<v-avatar size="60" color="blue" style="margin-top: 30px">
				<span class="white--text text-h5">{{ DmSenderAvatarName }}</span>
			</v-avatar>
			<v-list-item-content>
				<div class="text-overline mb-1">NEW DM</div>
				<v-list-item-title class="text-h5 mb-1">
					{{ DmSender }}
				</v-list-item-title>
				<v-list-item-subtitle>{{ DmMsg }}</v-list-item-subtitle>
			</v-list-item-content>
		</v-list-item>
		<div>
			<v-text-field v-model="quickReply" style="margin-left: 10px" label="Quick Reply" :rules="rules" hide-details="true"></v-text-field>
		</div>
		<v-card-actions>
			<v-btn outlined rounded text @click="sendQuickReply"> Reply </v-btn>
		</v-card-actions>
	</v-card>
</template>

<script>
	export default {
		props: ['DmUserID', 'DmSender', 'DmMsg'],
		data: () => ({
			rules: [(value) => !!value || 'Reply cannot be empty'],
			quickReply: '',
		}),
		computed: {
			DmSenderAvatarName() {
				return this.DmSender.substring(0, 1).toUpperCase()
			},
		},
		methods: {
			sendQuickReply() {
				const chatObj = {
					from: this.$store.state.user.userID,
					to: this.DmUserID,
					message: this.quickReply,
				}
				this.$store.commit('addChatHistory', {
					incoming: false,
					data: chatObj,
				})
				this.$store.state.user.webSocket.emit('send_chat', chatObj)
				this.quickReply = ''
				setTimeout(() => {
					const chatView = document.getElementById('chatView')
					if (chatView) chatView.scrollTop = chatView.scrollHeight
				}, 50)
			},
		},
	}
</script>
