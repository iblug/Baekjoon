import sys
input = sys.stdin.readline
while 1:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    s = sorted(s)
    if s[0] + s[1] <= s[2]:
        print('Invalid')
    else:
        s = set(s)
        if len(s) == 3:
            print('Scalene')
        elif len(s) == 2:
            print('Isosceles')
        else:
            print('Equilateral')