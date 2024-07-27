const inputs = require('fs').readFileSync('/dev/stdin').toString().split('\n')

let n = parseInt(inputs[0])
let s = inputs[1]
let r = 0
for (let i = 0; i < n; i++) {
  if (s[i] === 'j' || s[i] === 'i') {
    r += 2
  } else {
    r++
  }
}

console.log(r);