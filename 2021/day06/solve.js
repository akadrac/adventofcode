const { readFileSync } = require('fs');

const array = Array(9).fill(0)

const input = readFileSync(process.argv[2])
  .toString()
  .trim()
  .split(',')
  .map(e => { array[e++]++; return --e; })

const exit = 256
console.log(input)
console.log(array)

for (let i = 0; i < exit; i++) {
  // console.log(`day ${i} add index of ${i % 9} to ${(7 + i) % 9} value of ${array[i % 9]} to ${array[(7 + i) % 9]}`)
  array[(7 + i) % 9] += array[i % 9]
}

const result = array.reduce((a, c) => a + c, 0)
console.log(result)
