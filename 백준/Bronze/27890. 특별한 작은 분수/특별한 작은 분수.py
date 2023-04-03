x, n = map(int, input().split())
while n:
    if x & 1:
        x = (x*2)^6
    else:
        x = (x//2)^6
    n -= 1
print(x)