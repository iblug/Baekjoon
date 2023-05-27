n = input()
d = list(map(int, input().split()))
d = sorted(d)
if n == '1':
    print(d[0]**2)
else:
    print(d[0] * d[-1])
