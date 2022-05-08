const Mock = require('mockjs')
const Random = Mock.Random

const getAllUsers = function () {
	return [
		{ displayName: 'a', email: '1@1.com', user_id: '62620a8c04e7e8c9595c8294', active: false },
		{ displayName: 'bb', email: '1@12.com', user_id: '626954005f287336f4624973', active: true },
		{ displayName: 'cc', email: '1@12.cocm', user_id: '626954235f287336f4624974', active: true },
	]
}

const loginSuccess = function (options) {
	const email = JSON.parse(options.body)['email']
	if (email === '1@1.com')
		return { displayName: 'a', email: '1@12.com', user_id: '62620a8c04e7e8c9595c8294', settings: '#1c5c9c' }
	if (email === '1@12.com')
		return { displayName: 'bb', email: '1@12.com', user_id: '626954005f287336f4624973', settings: '#000000' }
	if (email === '1@12.cocm')
		return { displayName: 'cc', email: '1@12.com', user_id: '626954235f287336f4624974', settings: '#ffffff' }
}

const momentCreateSuccess = function () {
	return { moment_id: '62730811cf16ca91367916f5' }
}

const getChatHistoryBetweenTwoUsers = function (options) {
	const from_to = JSON.parse(options.body)
	const res = [
		{ from: from_to.from, to: from_to.to, message: Random.sentence(2), image: null },
		{ from: from_to.to, to: from_to.from, message: Random.sentence(2), image: null },
		{ from: from_to.from, to: from_to.to, message: Random.sentence(2), image: null },
	]
	return res
}

const getMoments = function () {
	const res = [
		{
			moment_id: '62730878cf16ca9136791707',
			from: '626954005f287336f4624973',
			time: 1651705976,
			content: 'aaaaaaaaaaaaaaa',
			image: ['8cbd3a2ac5b1c0119b65b67fd05a965c.png'],
			like: 0,
		},
		{
			moment_id: '62730876cf16ca9136791705',
			from: '626954005f287336f4624973',
			time: 1651705974,
			content: 'aaaaaaaaaaaaaaa',
			image: ['332dbe7abf9e420f8cf8c9b9218aa27f.png'],
			like: 0,
		},
		{
			moment_id: '62730876cf16ca9136791703',
			from: '626954005f287336f4624973',
			time: 1651705974,
			content: 'aaaaaaaaaaaaaaa',
			image: ['beaeb5a8186598c309552750fb0012c3.png'],
			like: 0,
		},
		{
			moment_id: '62730876cf16ca9136791701',
			from: '626954005f287336f4624973',
			time: 1651705974,
			content: 'aaaaaaaaaaaaaaa',
			image: ['91cfbba050ceeed919aa018a515f38cd.png'],
			like: 0,
		},
		{
			moment_id: '62730875cf16ca91367916ff',
			from: '626954005f287336f4624973',
			time: 1651705973,
			content: 'aaaaaaaaaaaaaaa',
			image: ['680f2a56c7041d03840534e8671768c9.png'],
			like: 0,
		},
	]
	return res
}
if (process.env.NODE_ENV === 'development') {
	Mock.mock('http://127.0.0.1:8080/allusers', 'get', getAllUsers)
	Mock.mock('http://127.0.0.1:8080/login', 'post', loginSuccess)
	Mock.mock('http://127.0.0.1:8080/chatHistory', 'post', getChatHistoryBetweenTwoUsers)
	Mock.mock('http://127.0.0.1:8080/moment/getRecentMoments', 'post', getMoments)
	Mock.mock('http://127.0.0.1:8080/moment/create', 'post', momentCreateSuccess)
}
