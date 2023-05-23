T = int(input())
for _ in range(T):
    a = int(input())
    d = 0
    r = []
    while a:
        if a%2:
            r.append(d)
        a //= 2
        d += 1
    print(' '.join(map(str, r)))