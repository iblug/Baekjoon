N, B = map(int, input().split())
r = []
while N > 0:
    if (n:=N%B) >= 10:
        n = chr(n+55)
    else:
        n = str(n)
    r.append(n)
    N = N//B
print(''.join(reversed(r)))
