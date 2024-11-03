n = int(input())
a = input()
b = input()
c = input()
d = input()

r = ''
f = True
for i in range(n):
    if a[i] == c[i]:
        if b[i] == d[i]:
            r += b[i]
        else:
            f = False
            break
if f:
    print(r)
else:
    print('htg!')