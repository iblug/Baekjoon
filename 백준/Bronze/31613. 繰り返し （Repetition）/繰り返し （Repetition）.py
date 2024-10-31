n = int(input())
m = int(input())

t = 0
while n < m:
    t += 1
    if n % 3 == 0:
        n += 1
    elif n%3 == 1:
        n *= 2
    else:
        n *= 3
print(t)