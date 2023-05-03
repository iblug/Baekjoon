import sys
input = sys.stdin.readline

n = int(input())
d = {}
r = []
for i in range(n):
    d[input().rstrip()] = i
for _ in range(n):
    r.append(input().rstrip())

c = 0
for i in range(n-1):
    for j in range(i+1, n):
        if d[r[i]] > d[r[j]]:
            c += 1
            break
print(c)