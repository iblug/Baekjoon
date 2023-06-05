n, b = input().split()
b = int(b)
t = 0
d = 0
for i in reversed(n):
    if i.isdigit():
        t += int(i)*b**d
    else:
        t += (ord(i)-55)*b**d
    d += 1
print(t)