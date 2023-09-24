n = int(input())
a = list(map(int, input().split()))
x = int(input())

a.sort()
s, e = 0, n-1
c = 0
while (s < e):
    if a[s] + a[e] < x:
        s += 1
    elif a[s] + a[e] > x:
        e -= 1
    else:
        c += 1
        s += 1
print(c)