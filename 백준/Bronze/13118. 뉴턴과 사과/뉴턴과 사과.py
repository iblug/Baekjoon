a = list(map(int, input().split()))
x, y, r = map(int, input().split())
t = 0
for i in range(4):
    if a[i] == x:
        t = i + 1
        break
print(t)