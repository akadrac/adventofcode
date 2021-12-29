const { readFileSync } = require('fs');

const size = process.argv[3]

const input = readFileSync(process.argv[2])
  .toString()
  .replace(/\r\n/g, '\n')
  .split('\n')
  .map(line => line.split(/[^\d]+/).map(num => Number(num)))
  .filter(e => e.length == 4)

const field = Array.from({ length: size }).fill(null).map(() => Array.from({ length: size }).fill(0))

for (const [x1, y1, x2, y2] of input) {
  // if (x1 != x2 && y1 != y2) continue

  let x = x1
  let y = y1

  while (true) {
    field[y][x]++

    if (x == x2 && y == y2) break

    if (x1 != x2) x1 < x2 ? x++ : x--
    if (y1 != y2) y1 < y2 ? y++ : y--
  }
}

const result = field.reduce((acc, cur) => acc + cur.filter(e => e > 1).length, 0)
console.log(result)
