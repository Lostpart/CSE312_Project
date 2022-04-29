const Mock = require('mockjs')
const Random = Mock.Random

const getAllUsers = function () {
	return [
		{ displayName: 'a', email: '1@1.com', user_id: '62620a8c04e7e8c9595c8294', active: false },
		{ displayName: 'bb', email: '1@12.com', user_id: '626954005f287336f4624973', active: true },
		{ displayName: 'cc', email: '1@12.cocm', user_id: '626954235f287336f4624974', active: true },
	]
}
Mock.mock('http://127.0.0.1:8080/allusers', 'get', getAllUsers)

const loginSuccess = function (options) {
	const email = JSON.parse(options.body)['email']
	if (email === '1@1.com') return { displayName: 'a', email: '1@12.com', user_id: '62620a8c04e7e8c9595c8294' }
	if (email === '1@12.com') return { displayName: 'bb', email: '1@12.com', user_id: '626954005f287336f4624973' }
	if (email === '1@12.cocm') return { displayName: 'cc', email: '1@12.com', user_id: '626954235f287336f4624974' }
}
Mock.mock('http://127.0.0.1:8080/login', 'post', loginSuccess)

const getChatHistoryBetweenTwoUsers = function (options) {
	const from_to = JSON.parse(options.body)
	const res = [
		{ from: from_to.from, to: from_to.to, message: Random.sentence(2), image: null },
		{ from: from_to.to, to: from_to.from, message: Random.sentence(2), image: null },
		{ from: from_to.from, to: from_to.to, message: Random.sentence(2), image: null },
	]
	return res
}
Mock.mock('http://127.0.0.1:8080/chatHistory', 'post', getChatHistoryBetweenTwoUsers)
