<template>
	<div class="tictactoe" >
		<div class="chess" style="margin-top:100px">
			<div class="row">
				<CellGrid @click="onClickCellGrid(0, $event)" :n="n" :finished="finished" />
				<CellGrid @click="onClickCellGrid(1, $event)" :n="n" :finished="finished" />
				<CellGrid @click="onClickCellGrid(2, $event)" :n="n" :finished="finished" />
			</div>
			<div class="row">
				<CellGrid @click="onClickCellGrid(3, $event)" :n="n" :finished="finished" />
				<CellGrid @click="onClickCellGrid(4, $event)" :n="n" :finished="finished" />
				<CellGrid @click="onClickCellGrid(5, $event)" :n="n" :finished="finished" />
			</div>
			<div class="row">
				<CellGrid @click="onClickCellGrid(6, $event)" :n="n" :finished="finished" />
				<CellGrid @click="onClickCellGrid(7, $event)" :n="n" :finished="finished" />
				<CellGrid @click="onClickCellGrid(8, $event)" :n="n" :finished="finished" />
			</div>
		</div>
		<div style="margin-top:30px">{{ result === null ? '' : `Result: ${result === 'draw' ? 'draw' : this.result + ' wins'}` }}</div>
	</div>
</template>

<script>
	import CellGrid from '@/components/CellGrid.vue'
	export default {
		components: { CellGrid },
		data() {
			return {
				n: 0,
				map: [
					[null, null, null],
					[null, null, null],
					[null, null, null],
				],
				result: null,
				finished: false,
			}
		},
		methods: {
			onClickCellGrid(i, text) {
				this.map[Math.floor(i / 3)][i % 3] = text
				this.n += 1
				this.checkWinner(i, text)
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
					this.result = text
					this.finished = true
					return
				}
				if (this.n === 9) {
					this.result = 'draw'
					this.finished = true
				}
			},
		},
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
