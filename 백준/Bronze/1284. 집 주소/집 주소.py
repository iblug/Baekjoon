import sys
input = sys.stdin.readline

l = {
    '0': 4,
    '1': 2,
    }
while True:
    s = input().rstrip()
    r = len(s) + 1
    if s == '0':
        break
    for e in s:
        r += l.get(e, 3)
    print(r)