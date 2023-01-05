# https://www.acmicpc.net/problem/18406

import time

n = list(map(int, input()))

start = time.time()

if sum(n[:len(n) // 2]) == sum(n[len(n) // 2:]):
    print('LUCKY')
else:
    print("READY")

end = time.time()

print(end - start)