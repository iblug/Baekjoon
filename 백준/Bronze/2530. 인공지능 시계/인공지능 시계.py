a, b, c = map(int, input().split())
d = int(input())
d += a*3600 + b*60 + c
c = d%60
d //= 60
b = d%60
d //= 60
a = d%24

print(a, b, c)