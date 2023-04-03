n = open(0)
c = 0
for e in n:
    a, b = e.split()
    b = int(b)
    if a == 'Es':
        c += b*21
    else:
        c += b*17
print(c)