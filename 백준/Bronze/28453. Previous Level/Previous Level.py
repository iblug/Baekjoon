t = int(input())
d = list(map(int, input().split()))
r = []
for e in d:
    if e < 250:
        r.append('4')
    elif e < 275:
        r.append('3')
    elif e < 300:
        r.append('2')
    else:
        r.append('1')
print(' '.join(r))