const { readFileSync } = require('fs');

const input = readFileSync(process.argv[2]).toString().replace(/\r\n/g, '\n').split('\n')

const looper = (list, index, control) => {
  if (list.length == 1) {
    console.log(`${list[0]} ${parseInt(list[0], 2)}`)
    return list[0]
  }
  let z = 0
  let o = 0

  list.forEach(element => {
    if (element[index] == 0) z += 1
    else o += 1
  })

  if (control == "high") return looper(list.filter(value => value[index] == z > o ? 0 : 1), index + 1, "high")
  if (control == "low") return looper(list.filter(value => value[index] == z > o ? 1 : 0), index + 1, "low")
}

const oxy = parseInt(looper(input, 0, "high"), 2)
const co2 = parseInt(looper(input, 0, "low"), 2)

console.log(oxy * co2)