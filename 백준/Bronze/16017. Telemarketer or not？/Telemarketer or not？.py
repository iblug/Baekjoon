import sys
input = sys.stdin.readline

s = [input().rstrip() for _ in range(4)]

if all([s[0] in '89', s[3] in '89']) and s[1] == s[2]:
    print('ignore')
else:
    print('answer')