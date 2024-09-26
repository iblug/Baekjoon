import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    now = 1
    r = 0
    for i in l:
        if i > 2*now:
            r += i - 2*now
        now = i
    print(r)