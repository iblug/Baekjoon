a, b, c, d = map(int, input().split())
t = a + d - b - c
if t < 0:
    print(-t)
else:
    print(t)