import sys
input = sys.stdin.readline

s = [input().rstrip() for _ in range(4)]

if any([s[0] not in '89', s[3] not in '89']):
    print('answer')
elif s[1] != s[2]:
    print('answer')
else:
    print('ignore')