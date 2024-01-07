a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = 0
for i in range(3):
    if (a[i] < b[i]):
        s += b[i] - a[i]
print(s)