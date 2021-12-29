const { readFileSync } = require('fs');

const array = readFileSync(process.argv[2]).toString().replace(/\r\n/g, '\n').split('\n')

const reducer = (acc, cur) => {
  const command = cur.split(/\s/)
  switch (command[0]) {
    case "forward": return { ...acc, forward: acc.forward + Number(command[1]), depth: acc.depth + Number(command[1]) * acc.aim }
    case "down": return { ...acc, aim: acc.aim + Number(command[1]) }
    case "up": return { ...acc, aim: acc.aim - Number(command[1]) }
    default: return acc
  }
}

const result = array.reduce(reducer, { forward: 0, aim: 0, depth: 0 })
console.log(result)
console.log(result.forward * result.depth)