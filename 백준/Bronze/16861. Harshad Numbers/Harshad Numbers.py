n = int(input())

m = n
while 1:
    t = m
    a = 0
    while t > 0:
        a += t%10
        t //= 10
    if m % a == 0:
        break
    m += 1
print(m)