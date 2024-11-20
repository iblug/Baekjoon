input()
s = input()
a = 0
c = 0

for l in s:
    if l == '1':
        a += 1
        c = 2
    elif c:
        a += 1
        c -= 1

print(a)