n, m, l = map(int, input().split())
r = 0
for i in range(n, m + 1):
    r += str(i).count(str(l))
print(r)