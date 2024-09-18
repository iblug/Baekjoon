n = int(input())
r = 0
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n):
    if a[i] > b[i]:
        r += 3
    elif a[i] == b[i]:
        r += 1
print(r)