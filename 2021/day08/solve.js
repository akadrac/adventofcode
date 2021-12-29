const { readFileSync } = require('fs')

const input = readFileSync(process.argv[2])
  .toString()
  .trim()
  .replace(/\r\n/g, '\n')
  .split('\n')
  .map(e => e.split(' | '))

// 1 = 2
// 7 = 3
// 4 = 4
// 8 = 7

const result = input.map(value => {

  const obj = {}

  value[0].split(' ').map(e => e.split("").sort().join("")).map(e => {

    switch (e.length) {
      case 2:
        obj[e] = 1
        obj[1] = e
        break
      case 3:
        obj[e] = 7
        obj[7] = e
        break
      case 4:
        obj[e] = 4
        obj[4] = e
        break
      case 7:
        obj[e] = 8
        obj[8] = e
        break
    }

    return e
  }).map(e => {

    const l = e.split("")

    if (obj[e]) return

    if (e.length == 5 && l.filter(i => obj[1].includes(i)).length == 2) {
      obj[e] = 3
      obj[3] = e
      return
    }
    if (e.length == 6 && l.filter(i => obj[4].includes(i)).length == 4) {
      obj[e] = 9
      obj[9] = e
      return
    }
    if (e.length == 6 && l.filter(i => obj[1].includes(i)).length == 2) {
      obj[e] = 0
      obj[0] = e
      return
    }
    if (e.length == 6) {
      obj[e] = 6
      obj[6] = e
      return
    }
    if (e.length == 5 && l.filter(i => obj[4].includes(i)).length == 3) {
      obj[e] = 5
      obj[5] = e
      return
    }
    if (e.length == 5) {
      obj[e] = 2
      obj[2] = e
      return
    }

  })



  const p1 = value[1].split(' ').map(e => e.split("").sort().join("")).reduce((a, c) => {
    // console.log(obj[c])
    return obj[c] ? ++a : a
  }, 0)

  const p2 = value[1].split(' ').map(e => e.split("").sort().join("")).map(e => obj[e]).join("")

  console.log(p2)
  // console.log(value)
  // console.log(obj)
  // console.log(r)
  return Number(p2)

}).reduce((a, c) => a + c, 0)

console.log(result)