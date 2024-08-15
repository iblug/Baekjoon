n = int(input())
y, m = 10 * n, 15 * n
l = list(map(int, input().split()))
for e in l:
    y += (e//30) * 10
    m += (e//60) * 15
if y > m:
    print('M', m)
elif y < m:
    print('Y', y)
else:
    print('Y', 'M', y)