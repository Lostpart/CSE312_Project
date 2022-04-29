export default {
	methods: {},
	state: {
		userID: null,
		email: null,
		displayName: null,
		chatHistory: {},
		usersList: [],
		webSocket: null,
		map:[]
	},
	mutations: {
		setMap(state,val) {
			state.map = val
		},
		setWebSocket(state, val) {
			state.webSocket = val
		},
		clearWebSocket(state) {
			state.webSocket = null
		},
		setUsersList(state, val) {
			state.usersList = val
		},
		clearUsersList(state) {
			state.usersList = null
		},
		setUserID(state, val) {
			state.userID = val
		},
		clearUserID(state) {
			state.userID = null
		},
		setEmail(state, val) {
			state.email = val
		},
		clearEmail(state) {
			state.email = null
		},
		setDisplayName(state, val) {
			state.displayName = val
		},
		clearDisplayName(state) {
			state.displayName = null
		},
		setChatHistory(state, chatHistoryObj) {
			state.chatHistory[chatHistoryObj['user_id']] = chatHistoryObj['history']
		},
		addChatHistory(state, chatObj) {
			if (chatObj['incoming']) {
				if (state.chatHistory[chatObj['data']['from']] === undefined) {
					state.chatHistory[chatObj['data']['from']] = []
				}
				chatObj['data']['flag'] = true
				state.chatHistory[chatObj['data']['from']].push(chatObj['data'])
			} else {
				if (state.chatHistory[chatObj['data']['to']] === undefined) {
					state.chatHistory[chatObj['data']['to']] = []
				}
				chatObj['data']['flag'] = false
				state.chatHistory[chatObj['data']['to']].push(chatObj['data'])
			}
		},
		clearChatHistory(state) {
			state.chatHistory = {}
		},
	},
}
