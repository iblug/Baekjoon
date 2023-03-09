n = int(input())
a = list(map(int, input().split()))
c = 0
if n > 2:
    while True:
        a = sorted(a,reverse=True)
        if a[0] == 0:
            break
        c += 1
        a[0] -= 1
        if a[1] > 0:
            a[1] -= 1
    if c > 1440:
        print(-1)
    else:
        print(c)
else:
    if max(a) > 1440:
        print(-1)
    else:
        print(max(a))