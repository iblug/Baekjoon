d = {}
n, m = map(int, input().split())
for i in range(n, m+1):
    while i > 0:
        d[i%10] = d.get(i%10, 0) + 1
        i //= 10

for i in range(10):
    print(d.get(i,0), end=' ')