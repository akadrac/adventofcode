const { readFileSync } = require('fs');

const size = Number(process.argv[3])
console.log(size)

const input = readFileSync(process.argv[2]).toString().replace(/\r\n/g, '\n').split('\n')

const array = Array(size * 2).fill(0)

const mapper = cur => {
  for (let i = 0; i < size; i++) {
    if (cur[i] == "0") array[i] += 1
    if (cur[i] == "1") array[i + size] += 1
  }
}

input.map(mapper)

const least = (array) => {
  let result = []
  for (let i = 0; i < size; i++) {
    if (array[i] < array[i + size]) result.push(0)
    else result.push(1)
  }
  return result
}

const most = (array) => {
  let result = []
  for (let i = 0; i < size; i++) {
    if (array[i] > array[i + size]) result.push(0)
    else result.push(1)
  }
  return result
}

console.log(array)
console.log(least(array))
console.log(most(array))

const l = least(array).join("")
const m = most(array).join("")

console.log(parseInt(l, 2) * parseInt(m, 2))

