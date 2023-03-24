a, b, c = map(int, input().split())
d = int(input())

c+=d
b += c//60
c = c%60
a += b//60
b %= 60

print(a%24, b, c)