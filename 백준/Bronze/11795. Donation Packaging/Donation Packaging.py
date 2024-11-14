n = int(input())
r = [0,0,0]
for _ in range(n):
    a, b, c = map(int, input().split())
    r[0] += a
    r[1] += b
    r[2] += c
    if r[0] < 30 or r[1] < 30 or r[2] < 30:
        print('NO')
    else:
        d = min(r)
        print(d)
        r[0] -= d
        r[1] -= d
        r[2] -= d