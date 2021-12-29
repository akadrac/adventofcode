const { readFileSync } = require('fs');

const input = readFileSync(process.argv[2]).toString().replace(/\r\n/g, '\n').split('\n')

const numbers = input[0].split(',')
const boardInput = input.slice(1)

const boards = []
let board = 0

boardInput.map((line, index) => {
  const ln = (index) % 6
  if (ln == 0) {
    boards[board] = []
    board++
  } else {
    const n = /^([\d|\s]\d)\s([\d|\s]\d)\s([\d|\s]\d)\s([\d|\s]\d)\s([\d|\s]\d)/.exec(line)
    boards[board - 1][ln - 1] = [[Number(n[1]), false], [Number(n[2]), false], [Number(n[3]), false], [Number(n[4]), false], [Number(n[5]), false]]
  }
})
boards.pop()

console.log(`number of numbers: ${numbers.length}`)
console.log(`number of boards: ${boards.length}`)

let winner
let winningNumber

let winners = []

const bingo = () => {
  for (let b = 0; b < boards.length; b++) {
    if (winners.includes(b)) continue
    const board = boards[b]
    for (let c = 0; c < 5; c++) {
      if (board[c][0][1] == true && board[c][1][1] == true && board[c][2][1] == true && board[c][3][1] == true && board[c][4][1] == true) {
        console.log(`board r ${b} won`)
        winners.push(b)
        break
      }
      if (board[0][c][1] == true && board[1][c][1] == true && board[2][c][1] == true && board[3][c][1] == true && board[4][c][1] == true) {
        console.log(`board c ${b} won`)
        winners.push(b)
        break
      }
    }
  }
}

for (let i = 0; i < numbers.length; i++) {
  for (const board of boards) {
    for (const item of board) {
      for (let n = 0; n < item.length; n++) {
        if (item[n][0] == numbers[i]) item[n][1] = true
      }
    }
  }
  if (i > 5) {
    bingo()
    console.log(`winning boards: ${winners.length}`)
    if (winners.length == boards.length) {
      winningNumber = numbers[i]
      break
    }
  }
}

const matched = []
const nomatch = []

let lastBoard = winners.pop()
console.log(lastBoard)
winner = boards[lastBoard]
console.log(winner)
for (const item of winner) {
  for (let n = 0; n < item.length; n++) {
    item[n][1] ? matched.push(item[n][0]) : nomatch.push(item[n][0])
  }
}

const m = matched.reduce((acc, cur) => acc + cur, 0)
const n = nomatch.reduce((acc, cur) => acc + cur, 0)

// console.log(winner)
console.log(`winningNumber: ${winningNumber}`)

// console.log(nomatch)
console.log(`calc of board numbers ${n}`)

console.log(`score: ${n * winningNumber}`)
