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

let winner
let winningNumber

const bingo = (theNumber) => {
  for (const board of boards) {
    for (const item of board) {
      if (item[0][1] == true && item[1][1] == true && item[2][1] == true && item[3][1] == true && item[4][1] == true) {
        winner = board
        return true
      }
    }
    for (let c = 0; c < 5; c++) {
      if (board[0][c][1] == true && board[1][c][1] == true && board[2][c][1] == true && board[3][c][1] == true && board[4][c][1] == true) {
        winner = board
        return true
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
  if (i > 5) if (bingo()) {
    winningNumber = numbers[i]
    break
  }
}

const matched = []
const nomatch = []

if (winner) {
  for (const item of winner) {
    for (let n = 0; n < item.length; n++) {
      item[n][1] ? matched.push(item[n][0]) : nomatch.push(item[n][0])
    }
  }

  const m = matched.reduce((acc, cur) => acc + cur, 0)
  const n = nomatch.reduce((acc, cur) => acc + cur, 0)

  console.log(winner)
  console.log(winningNumber)

  console.log(n)

  console.log(n * winningNumber)
} else {
  console.log("no winner")
}