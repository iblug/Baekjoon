n, a, b, c, d = map(int, input().split())

if n % a == 0:
    k = n//a * b
else:
    k = (n//a + 1) * b

if n % c == 0:
    j = n//c * d
else:
    j = (n//c + 1) * d

print(min(k, j))
