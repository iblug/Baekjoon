a, b = map(int, input().split())
c = a + b
d = a - b
[print(c, d, sep='\n') if c > d else print(d, c, sep='\n')]