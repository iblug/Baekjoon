def com(c, p):
    global r
    l = len(c)
    if c and c[-1] == a[l-1]:
        p += 1
    if l == 10:
        if p >= 5:
            r += 1
        return

    for j in range(1, 6):
        if l >= 2 and c[-2] == c[-1] == j:
            continue
        c.append(j)
        com(c, p)
        c.pop()

a = list(map(int, input().split()))
r = 0
com([],0)
print(r)