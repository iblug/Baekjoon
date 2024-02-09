import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().rstrip()
    if 'D' in s:
        print(s.index('D'))
    else:
        print(len(s))