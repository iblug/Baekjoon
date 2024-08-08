n, m, k, a, b, c = map(int, input().split())
t = max(n*a, m*b, k*c)
if n*a == t:
    print('Joffrey', end=' ')
if m*b == t:
    print('Robb', end=' ')
if k*c == t:
    print('Stannis')