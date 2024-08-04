const inputs = require('fs').readFileSync('/dev/stdin').toString().split('\n')

console.log(Math.min(parseInt(inputs[0]), parseInt(inputs[1]))*50)
