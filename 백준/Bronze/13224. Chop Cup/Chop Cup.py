s = input()
l = [True, False, False]
for e in s:
    if e == 'A':
        l[0], l[1] = l[1], l[0]
    elif e == 'B':
        l[1], l[2] = l[2], l[1]
    else:
        l[0], l[2] = l[2], l[0]
print(l.index(True) + 1)