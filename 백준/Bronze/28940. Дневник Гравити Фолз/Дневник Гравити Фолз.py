import math

w, h = map(int, input().split())
n, a, b = map(int, input().split())
c = w//a
d = h//b
if c * d:
    print(math.ceil(n / (c * d)))
else:
    print(-1)