import math
a, b, c = map(int, input().split())
if b-a < 0 :
    print(0)
else:
    print(math.ceil((b-a)/c))