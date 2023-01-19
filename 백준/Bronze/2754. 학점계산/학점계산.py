a,*b = input()
c = float('FDCBA'.find(a))
if b:
    if b[0] == '+':
        c += 0.3
    elif b[0] == '-':
        c -= 0.3
    else:
        pass
print(c)