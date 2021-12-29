const { readFileSync } = require('fs');

const array = readFileSync(process.argv[2]).toString().replace(/\r\n/g, '\n').split('\n')

const stop = array.length - 2
const reducer = (acc, cur, index, arr) => {
  if (index < stop) return [...acc, Number(arr[index]) + Number(arr[index + 1]) + Number(arr[index + 2])]
  return acc
}

const count = (acc, cur, index, array) => {
  if (index == 0) return acc

  if (Number(array[index]) > Number(array[index - 1])) return acc += 1

  return acc
}
console.log(array.reduce(reducer, []).reduce(count, 0))