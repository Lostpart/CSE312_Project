<template>
	<div class="tictactoe" style="margin-top: 200px">
		<div class="row">
			<CellGrid @click="onClickCellGrid(0, $event)" i="0" />
			<CellGrid @click="onClickCellGrid(1, $event)" i="1" />
			<CellGrid @click="onClickCellGrid(2, $event)" i="2" />
		</div>
		<div class="row">
			<CellGrid @click="onClickCellGrid(3, $event)" i="3" />
			<CellGrid @click="onClickCellGrid(4, $event)" i="4" />
			<CellGrid @click="onClickCellGrid(5, $event)" i="5" />
		</div>
		<div class="row">
			<CellGrid @click="onClickCellGrid(6, $event)" i="6" />
			<CellGrid @click="onClickCellGrid(7, $event)" i="7" />
			<CellGrid @click="onClickCellGrid(8, $event)" i="8" />
		</div>
		<div style="margin-top: 30px">
			<v-btn elevation="2" v-show="finished">{{ 'Result: ' + (result === 'draw' ? 'draw' : result + ' wins') }}</v-btn>
		</div>
		<div>
			<v-btn elevation="2" v-show="finished" style="margin-top: 20px" @click="resetMap">RESET</v-btn>
		</div>
		<div>
			<v-btn elevation="2" v-show="!finished" style="margin-top: 20px" @click="resetMap">NEXT:{{ nextPlayer }}</v-btn>
		</div>
	</div>
</template>

<script>
	import CellGrid from '@/components/CellGrid.vue'
	export default {
		components: {
			CellGrid,
		},
		data() {
			return {
				updated: true,
			}
		},
		watch: {
			map() {
				this.updated = false
				this.$nextTick(() => {
					this.updated = true
				})
			},
		},
		computed: {
			nextPlayer() {
				return this.$store.state.user.n % 2 == 0 ? 'x' : 'o'
			},
			map() {
				return this.$store.state.user.map
			},
			result() {
				return this.$store.state.user.result
			},
			finished() {
				return this.$store.state.user.finished
			},
			n() {
				return this.$store.state.user.n
			},
		},
		methods: {
			resetMap() {
				this.$store.state.user.webSocket.emit('update_map', {
					map: [
						[null, null, null],
						[null, null, null],
						[null, null, null],
					],
					result: null,
					finished: false,
					n: 0,
				})
			},
			onClickCellGrid(i) {
				if (this.finished) return
				const text = this.n % 2 === 0 ? 'x' : 'o'
				this.$store.commit('setN', this.n + 1)
				this.$store.commit('updateMap', { i: i, text: text })
				this.checkWinner(i, text)
				const map = this.$store.state.user.map
				const result = this.$store.state.user.result
				const finished = this.$store.state.user.finished
				const n = this.$store.state.user.n
				this.$store.state.user.webSocket.emit('update_map', { map: map, result: result, finished: finished, n: n })
			},
			checkWinner(i, text) {
				const currRow = Math.floor(i / 3)
				const currCol = i % 3
				const map = this.map
				if (
					(map[currRow][0] === text && map[currRow][1] === text && map[currRow][2] === text) ||
					(map[0][currCol] === text && map[1][currCol] === text && map[2][currCol] === text) ||
					(map[0][0] === text && map[1][1] === text && map[2][2] === text) ||
					(map[2][0] === text && map[1][1] === text && map[0][2] === text)
				) {
					this.$store.commit('setResult', text)
					this.$store.commit('setFinished', true)
					return
				}
				if (this.n === 9) {
					this.$store.commit('setResult', 'draw')
					this.$store.commit('setFinished', true)
				}
			},
		},
		mounted() {},
	}
</script>

<style>
	.tictactoe {
		display: flex;
		justify-content: center;
		align-items: center;
		flex-direction: column;
	}
	.row {
		display: flex;
	}
</style>
