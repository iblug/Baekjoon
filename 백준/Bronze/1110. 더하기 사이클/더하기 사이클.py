s = int(input())
c = 0
n = -1

x = s // 10
y = s % 10

while s != n:
    n = 10*y + (x + y)%10
    x = n // 10
    y = n % 10
    c += 1
print(c)