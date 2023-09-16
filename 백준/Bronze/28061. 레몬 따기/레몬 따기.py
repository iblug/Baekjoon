n = int(input())
a = list(map(int, input().split()))
r = 0
for i in range(n):
    t = a[i] - n + i
    if t > r:
        r = t
print(r)