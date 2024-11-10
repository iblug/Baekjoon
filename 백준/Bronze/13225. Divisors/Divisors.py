import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        if n%i == 0:
            cnt += 1
    print(n, cnt)