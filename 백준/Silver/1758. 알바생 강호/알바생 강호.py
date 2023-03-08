import sys
input = sys.stdin.readline

n = int(input())

t = [int(input()) for _ in range(n)]
t = sorted(t, reverse=True)
cnt = 0
for i in range(n):
    if t[i]-i > 0:
        cnt += t[i]-i
    else:
        break
print(cnt)