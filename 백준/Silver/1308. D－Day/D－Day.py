import datetime as dt

y1, m1, d1 = map(int, input().split())
start = dt.date(y1, m1, d1)
y2, m2, d2 = map(int, input().split())
end = dt.date(y2, m2, d2)

if end >= dt.date(y1+1000, m1, d1):
    print('gg')
else:
    print(f'D-{(end - start).days}')