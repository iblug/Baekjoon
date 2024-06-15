import sys
input = sys.stdin.readline

n, k = map(int, input().split())
r = 0
t = 0

for _ in range(n):
    s = input().rstrip()
    if s == 'save':
        r = t
    elif s == 'load':
        t = r
    elif s == 'shoot':
        t -= 1
    else:
        t += k
    print(t)