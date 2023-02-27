n, k = map(int, input().split())

i = 0
while k and i <= n:
    i += 1
    if not n % i:
        k -= 1
if k:
    print(0)
else:
    print(i)