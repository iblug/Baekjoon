def f(c, p):
    if (l:=len(c)) == 10:
        if p >= 5:
            r[0] += 1
        return

    for j in range(1, 6):
        if l >= 2 and c[-2] == c[-1] == j:
            continue
        c.append(j)
        if j == a[l]:
            f(c, p+1)
        else:
            f(c, p)
        c.pop()

a = list(map(int, input().split()))
r = [0]
f([],0)
print(r[0])