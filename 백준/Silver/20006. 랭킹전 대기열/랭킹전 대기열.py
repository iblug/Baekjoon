import sys
input = sys.stdin.readline

p, m = map(int, input().split())
t = []

for _ in range(p):
    a = input().rstrip().split()
    f = 0
    a[0] = int(a[0])
    for i in t:
        if len(i) == m:
            continue
        if i[0][0]-10 <= a[0] <= i[0][0]+10:
            i.append(a)
            f = 1
            break
    if not f:
        t.append([a])

for i in t:
    if len(i) == m:
        print('Started!')
    else:
        print('Waiting!')
    k = sorted(i, key=lambda x: x[1])
    for j in k:
        print(' '.join(map(str,j)))