const { readFileSync } = require('fs')

const input = readFileSync(process.argv[2])
  .toString()
  .trim()
  .split(',')
  .map(Number)
  .filter(e => e != NaN)
  .sort((a, b) => a - b)

const mean = (array) => array.reduce((a, c) => a + c, 0) / array.length
const standardDeviation = (array, mean) => Math.sqrt(input.reduce((a, c) => a + Math.pow(c - mean, 2)), 0) / (array.length - 1)
const sum = (v, r = 0) => v == 0 ? r : sum(v - 1, r + v)

const m = Math.floor(mean(input))
const median = input[input.length / 2]
// const sd = standardDeviation(input, m)
// const r = Math.round(sd)

console.log(m)
// console.log(sd)
// console.log(r)

const resultp1 = input.reduce((a, c) => a + Math.abs(c - median), 0)
const resultp1b = input.reduce((a, c) => a + sum(Math.abs(c - median)), 0)

const resultp2 = input.reduce((a, c) => a + sum(Math.abs(c - m)), 0)

console.log(resultp2)
