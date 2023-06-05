n, b = input().split()
b = int(b)
t = 0
i = len(n) - 1
d = 0
while i >= 0:
    if n[i].isdigit():
        t += int(n[i])*b**d
    else:
        t += (ord(n[i])-ord('A')+10)*b**d
    d += 1
    i -= 1
print(t)