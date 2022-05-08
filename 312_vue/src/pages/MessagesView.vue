<template>
	<div>
		<ContactsList v-show="this.$store.state.user.loggedIn"></ContactsList>
		<h1 v-show="!this.$store.state.user.loggedIn"> You haven't signed in</h1>
	</div>
</template>

<script>
	// @ is an alias to /src
	import ContactsList from '@/components/ContactsList'

	export default {
		name: 'MessagesView',
		components: {
			ContactsList,
		},
	}
</script>
