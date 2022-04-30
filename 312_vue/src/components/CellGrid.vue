<template>
	<div>
		<div class="cell" v-on:click="onClickSelf">
			<template>{{ text }}</template>
		</div>
	</div>
</template>

<script>
	export default {
		props: ['n', 'finished', 'i'],
		data() {
			return {
				text: '',
			}
		},
		computed: {
		},
		methods: {
			onClickSelf() {
				if (this.finished) {
					return
				}
				if (this.text && this.text !== '') {
					return
				}
				this.a = true
				this.$emit('click', this.text)
			},
		},
		mounted() {
			const row = Math.floor(this.i / 3)
			const col = this.i % 3
			setInterval(() => {
				try {
					this.text = this.$store.state.user.map[row][col]
				} catch (err) {
					// console.log(row, col)
				}
			}, 200)
		},
	}
</script>

<style>
	.cell {
		border: 1px solid black;
		width: 100px;
		height: 100px;
		display: flex;
		justify-content: center;
		align-content: center;
		font-size: 65px;
	}
</style>
