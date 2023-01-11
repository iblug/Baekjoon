T = int(input())

for _ in range(T):
    h, _, n = map(int, input().split())
    if n % h == 0:
        c = h
        r = n // h
    else:
        c = n % h
        r = n // h + 1
    print(100*c + r)