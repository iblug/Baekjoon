import datetime as dt

y1, m1, d1 = map(int, input().split())
start = dt.date(y1, m1, d1)
y2, m2, d2 = map(int, input().split())
end = dt.date(y2, m2, d2)

if y2 - y1 > 1000:
    print('gg')
elif y2 - y1 == 1000 and m1 < m2:
    print('gg')
elif y2 - y1 == 1000 and m1 == m2 and d1 <= d2:
    print('gg')
else:
    print(f'D-{(end - start).days}')
