import sys
input = sys.stdin.readline

d = {
    'Q1': 0,
    'Q2': 0,
    'Q3': 0,
    'Q4': 0,
    'AXIS': 0,
}

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    if x*y > 0:
        if x > 0:
            d['Q1'] += 1
        else:
            d['Q3'] += 1
    elif x*y<0:
        if x > y:
            d['Q4'] += 1
        else:
            d['Q2'] += 1
    else:
        d['AXIS'] += 1

for k, v in d.items():
    print(f'{k}: {v}')