import sys
from itertools import permutations
input = sys.stdin.readline

d = list(permutations(map(str, range(1, 10)), 3))

n = int(input())
data = []
for _ in range(n):
    a, b, c = input().split()
    data.append((a, int(b), int(c)))
cnt = 0
for num in d:
    f = 0
    for e in data:
        a, s, b = e
        for i in range(3):
            if a[i] == num[i]:
                s -= 1
                if s < 0:
                    f = 1
                    break
            elif a[i] in num:
                b -= 1
                if b < 0:
                    f = 1
                    break
        if s != 0 or b != 0:
            f = 1
        if f:
            break
    if f:
        continue
    cnt += 1            
print(cnt)