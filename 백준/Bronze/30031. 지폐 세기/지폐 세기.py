a = open(0).read().split()
r = 0
for l in a[1::2]:
    if l == '136':
        r += 1000
    elif l == '142':
        r += 5000
    elif l == '148':
        r += 10000
    else:
        r += 50000
print(r)