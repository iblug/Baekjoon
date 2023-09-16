n = int(input())
d = list(map(int, input().split()))

c = 1
for i in range(1, n):
    if d[i] >= d[i-1]:
        c += 1
print(c)
