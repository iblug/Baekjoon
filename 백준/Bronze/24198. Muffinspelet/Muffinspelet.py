n = int(input())
a, b = 0, 0
r = 0
t = 1
while n > 0:
    r = n//2
    if t == 1:
        b += n-r
    else:
        a += n-r
    n = r
    t *= -1
print(a, b)