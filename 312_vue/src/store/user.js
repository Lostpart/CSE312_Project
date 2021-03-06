export default {
	methods: {},
	state: {
		userID: null,
		email: null,
		displayName: null,
		chatHistory: {},
		usersList: [],
		webSocket: null,
		map: [
			[null, null, null],
			[null, null, null],
			[null, null, null],
		],
		n: 0,
		result: null,
		finished: false,
		momentsList: [],
		color: '#bfdefc',
		loggedIn: false
	},
	mutations: {
		setLoggedIn(state, val) {
			state.loggedIn = val
		},
		setColor(state, val) {
			state.color = val
		},
		clearColor(state) {
			state.color = '#bfdefc'
		},
		setMomentsList(state, val) {
			state.momentsList = val
		},
		updateMomentsList(state, momentLikeObj) {
			const momentToUpdateID = momentLikeObj['moment_id']
			for (let i = 0; i < state.momentsList.length; i++) {
				const moment = state.momentsList[i]
				if (moment['moment_id'] === momentToUpdateID) {
					state.momentsList[i]['like'] = momentLikeObj['like']
					return
				}
			}
		},
		setMap(state, val) {
			state.map = val
		},
		setN(state, val) {
			state.n = val
		},
		setResult(state, val) {
			state.result = val
		},
		setFinished(state, val) {
			state.finished = val
		},
		updateMap(state, updateObj) {
			const i = updateObj['i']
			const text = updateObj['text']
			const row = Math.floor(i / 3)
			const col = i % 3
			state.map[row][col] = text
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
				chatObj['data']['flag'] = true
				if (!state.chatHistory[chatObj['data']['from']]) state.chatHistory[chatObj['data']['from']] = []
				state.chatHistory[chatObj['data']['from']].push(chatObj['data'])
			} else {
				chatObj['data']['flag'] = false
				if (!state.chatHistory[chatObj['data']['to']]) state.chatHistory[chatObj['data']['to']] = []
				state.chatHistory[chatObj['data']['to']].push(chatObj['data'])
			}
		},
		clearChatHistory(state) {
			state.chatHistory = {}
		},
	},
}
