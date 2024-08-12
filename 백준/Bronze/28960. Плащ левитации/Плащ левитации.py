h, l, a, b = map(int, input().split())
if h >= a and l >= a and h >= b and l >= b:
    print('YES')
elif (h >= a/2 and l >= b) or (l >= a and h >= b/2):
    print('YES')
else:
    print('NO')