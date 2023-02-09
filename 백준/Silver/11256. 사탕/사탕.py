import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    j, n = map(int, input().split())
    h = []
    for _ in range(n):
        a, b = map(int, input().split())
        h.append(a*b)
    h.sort(reverse=True)
    cnt = 0
    for i in h:
        j -= i
        cnt += 1
        if j <= 0:
            break
    print(cnt)