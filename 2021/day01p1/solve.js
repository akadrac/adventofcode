const { readFileSync } = require('fs');

const array = readFileSync(process.argv[2]).toString().replace(/\r\n/g,'\n').split('\n')

// fs.readFile('input.txt', 'utf8', (err, data) => {
//   const rows = data.split(/\r?\n/)
//   console.log(rows.reduce(reducer, 0))
// })

const reducer = (acc, cur, index, array) => {
  if (index == 0) return acc

  if (Number(array[index]) > Number(array[index - 1])) return acc += 1

  return acc
}

console.log(array.reduce(reducer, 0))